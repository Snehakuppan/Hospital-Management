                  /*HOSPITAL MANAGEMENT*/
use [d2manalysistraining];

select * from[dbo].[sk_patient_details];
select * from [dbo].[sk_patient_profile];
select * from [dbo].[sk_admission_details];
select * from [dbo].[sk_doctor_details];
select * from [dbo].[sk_payment];

/*procedure-1 to insert values into patient_details table*/
create or alter procedure sk_patient_details_dml
(@Patient_id int ,
@Case_id int  ,
@Patient_disease varchar(100) ,
@Patient_condition_critical varchar(100),
@Doctor_id varchar(100) ,
@Doctor_name varchar(100),
@select_operation varchar(10)='',
@condition varchar(100)='',
@update_condition varchar(100)=''
)
as
begin
IF @select_operation='insert'
begin
insert into sk_patient_details(Patient_id,Case_id,Patient_disease,Patient_condition_critical,Doctor_id,Doctor_name)
values
(@Patient_id,@Case_id,@Patient_disease,@Patient_condition_critical,@Doctor_id,@Doctor_name)
PRINT 'Insert Statement Executed Successfully ';
end
else if @select_operation='update'
begin
update sk_patient_details set Patient_disease= @update_condition where  Case_id= @condition 
PRINT 'Update Statement Executed Successfully ';
end
else
begin
delete from sk_patient_details where Case_id = @condition 
PRINT 'Delete Statement Executed Successfully ';
end
end


/*procedure2 - to insert value into patient_profile table*/
create or alter procedure sk_patient_profile_dml
(@Patient_id int,
@Patient_name varchar(50),
@Patient_age int,
@Patient_dob date,
@Patient_gender varchar(50),
@Patient_address varchar(50),
@Patient_email varchar(50),
@Patient_phoneno bigint,
@Patient_adhaarno bigint,
@Patient_bloodgroup varchar(50),
@select_operation varchar(10)='',
@condition varchar(100)='',
@update_condition varchar(100)=''
)
as
begin
IF @select_operation='insert'
begin
insert into [sk_patient_profile](Patient_id,Patient_name,Patient_age,Patient_dob,Patient_gender,Patient_address,Patient_email,Patient_phoneno,Patient_adhaarno,Patient_bloodgroup)
values
(@Patient_id,@Patient_name,@Patient_age,@Patient_dob,@Patient_gender,@Patient_address,@Patient_email,@Patient_phoneno,@Patient_adhaarno,@Patient_bloodgroup)
PRINT 'Insert Statement Executed Successfully ';
end
else if @select_operation='update'
begin
update [sk_patient_profile] set Patient_name = @update_condition where Patient_id = @condition 
PRINT 'Update Statement Executed Successfully ';
end
else
begin
delete from [sk_patient_profile]  where Patient_id = @condition  
PRINT 'Delete Statement Executed Successfully ';
end
end


/*view1- to combile admission and payment table*/
go
CREATE VIEW
sk_final_payment
as 
select  [sk_payment].[Case_id],[dbo].[sk_payment].[Lab_charge],[dbo].[sk_payment].[Scan_charge],
[dbo].[sk_payment].[Doctor_charge],[dbo].[sk_payment].[Pharmacy_bill],[dbo].[sk_admission_details].[room_bill] from [dbo].[sk_admission_details] full outer join
[dbo].[sk_payment] on [dbo].[sk_admission_details].[case_id]=[dbo].[sk_payment].[Case_id]
select * from sk_final_payment;


/*function1-to find patient room*/
create function sk_find_patient_room(@case_id int)
returns varchar(50)
as
begin 
return (select [Block_floor_roomno] from [dbo].[sk_admission_details] where Case_id=@Case_id)

end

select[dbo].[sk_find_patient_room] (112) as roomno;



/*function 2 - to find no of days patient admitted in hospital*/
create function sk_patient_admit_days(@case_id int)
returns int
as
begin
return (select datediff(day,admission_date,admission_end_date) from [dbo].[sk_admission_details] where case_id=@case_id)
end

select [dbo].[sk_patient_admit_days](113) as total;



/*function 3 to find total bill amount of patient*/
CREATE FUNCTION sk_total_bill (@Case_id int)
returns int
as
begin
return (select (Doctor_charge+Lab_charge+Pharmacy_bill+isnull(room_bill,0)+isnull(Scan_charge,0)) as totalbill
		from sk_final_payment where Case_id=@Case_id)
end
select[dbo].[sk_total_bill] (113) as totalbill;



/*function-4 to find the total case for particular disease*/
create function sk_total_case(@patient_disease varchar(50))
returns int
as
begin
return (select count(*) from sk_patient_details as total_dengue where Patient_disease=@patient_disease)
end

select [dbo].[sk_total_case]('dengue') as total_cases

/*procedure 3 -to create a table*/
create or alter procedure sk_patient_profile2
as
begin
create table sk_deleted_profile_datas
(patient_id int primary key,
Patient_name varchar(50),
Patient_age int,
patient_dob date,
Patient_gender varchar(50),
Patient_address varchar(100),
Patient_email varchar(50),
Patient_phoneno bigint,
Patient_adhaarno bigint,
Patient_bloodgroup varchar(50))
end

/*trigger 1 back up for patient_profile*/
create or alter trigger sk_patient_profile_delete_trigger
on sk_patient_profile
after delete
as
begin
insert into sk_deleted_profile_datas
(patient_id,Patient_name,Patient_age,patient_dob,Patient_gender,Patient_address,Patient_email,Patient_phoneno,Patient_adhaarno,Patient_bloodgroup)
select 
del.Patient_id,del.Patient_name,del.Patient_age,del.Patient_dob,del.Patient_gender,del.Patient_address,del.Patient_email,del.Patient_phoneno,del.Patient_adhaarno,del.Patient_bloodgroup
from deleted del
end;

delete from sk_patient_profile where Patient_id=102;

select * from sk_deleted_profile_datas;


/*view 2 this view is to analyze the critical_ patient month wise*/ 
create view sk_criticalpatient_month as
select count(*) as patientcount,substring(cast(admission_date as varchar(10)),1,7)as admission_date from dbo.sk_admission_details group by substring(cast(admission_date as varchar(10)),1,7);


/*view 3 this view is to analyze the no of patient affected */ 
create view sk_patient_vs_disease as
select count(*)as patient, Patient_disease from sk_patient_details group by Patient_disease ;


/*view 4 this view is to get the count of critical patient bloodgroup*/
create view sk_bloodbank as
select count(*)as cnt,a.Patient_bloodgroup from (select  dtl.Patient_id, Patient_bloodgroup from sk_patient_details as dtl left outer join sk_patient_profile as prf 
on dtl.Patient_id=prf.Patient_id where Patient_condition_critical='yes') as a group by a.Patient_bloodgroup;



