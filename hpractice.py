from tkinter import *
import tkinter as ttk
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox

from tkcalendar import Calendar,DateEntry
import pyodbc as py
server = 'd2mtrainingdb.database.windows.net'
db = 'd2manalysistraining'
user = 'dbtuser'
pwd = 'Disys@2022'
conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                      ';DATABASE=' + db +
                      '; UID=' + user +
                      '; PWD=' + pwd +
                      ';Trusted_Connection=no')
cursor = conn.cursor()


class hospital:
    def __init__(self,root):
        #main frame
        self.root=root
        self.root.title("HOSPITAL MANAGEMENT")
        self.root.geometry("1500x900")
        
        
        self.Patient_id=StringVar()
        self.Patient_name=StringVar()
        self.Patient_age=StringVar()
        self.Patient_dob=StringVar()
        self.Patient_gender=StringVar()
        self.Patient_address=StringVar()
        self.Patient_email=StringVar()
        self.Patient_phoneno=StringVar()
        self.Patient_adhaarno=StringVar()
        self.Patient_bloodgroup=StringVar()

        
        
        self.root.configure(background='#2C2D2B')
        self.root.photo=PhotoImage(file=r"Hospital_Icon.png")
        self.root.iconphoto(False,self.root.photo)
        labeltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("Arial Black",50))
        labeltitle.pack(side=TOP,fill=X)

        

        #subframe1
        frame1=Frame(self.root,bd=10,relief=RIDGE)
        frame1.place(x=0,y=100,width=1359,height=400)

        
        #subframe1 left
        frameleft=LabelFrame(frame1,bd=10,relief=RIDGE,text="ENTRY",font=("Arial Black",30))
        frameleft.place(x=0,y=5,width=1000,height=370)

        #subframe1 right
        viewframe=LabelFrame(frame1,bd=10,relief=RIDGE,text="VIEWBOX",font=("Arial Black",30))
        viewframe.place(x=990,y=5,width=350,height=370)

        #subframe2
        buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        buttonframe.place(x=0,y=500,width=1353,height=70)

        #subframe3
        Detailframe=Label(self.root,bd=10,relief=RIDGE)
        Detailframe.place(x=0,y=550,width=1353,height=150)

        #labelbox
        label1=Label(frameleft,text="Patient id",font=("Calibri",20),padx=2)
        label1.grid(row=0,column=0,sticky="w")

        label2=Label(frameleft,text="Patient name",font=("Calibri",20),padx=2)
        label2.grid(row=1,column=0,sticky="w")

        label3=Label(frameleft,text="Patient age",font=("Calibri",20),padx=2)
        label3.grid(row=2,column=0,sticky="w")

        label4=Label(frameleft,text="Patient dob",font=("Calibri",20),padx=2)
        label4.grid(row=3,column=0,sticky="w")

        label5=Label(frameleft,text="Patient gender",font=("Calibri",20),padx=2)
        label5.grid(row=4,column=0,sticky="w")

        label6=Label(frameleft,text="Patient address",font=("Calibri",20),padx=2)
        label6.grid(row=0,column=2,sticky="w")

        label7=Label(frameleft,text="Patient email",font=("Calibri",20),padx=2)
        label7.grid(row=1,column=2,sticky="w")

        label8=Label(frameleft,text="Patient phoneno",font=("Calibri",20),padx=2)
        label8.grid(row=2,column=2,sticky="w")

        label9=Label(frameleft,text="Patient adhaarno",font=("Calibri",20),padx=2)
        label9.grid(row=3,column=2,sticky="w")

        label10=Label(frameleft,text="Patient bloodgroup",font=("Calibri",20),padx=2)
        label10.grid(row=4,column=2,sticky="w")


        #entrybox
        entry1=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_id)
        entry1.grid(row=0,column=1)

        entry2=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_name)
        entry2.grid(row=1,column=1)

        entry3=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_age)
        entry3.grid(row=2,column=1)

        #entry4=Entry(frameleft,font=("Calibri",20),width=20)
        #entry4.grid(row=3,column=1)

        c1=DateEntry(frameleft,font=("Calibri",20),width=19,bg="darkblue",fg="white",textvariable=self.Patient_dob)
        c1.grid(row=3,column=1)

        #entry5=Entry(frameleft,font=("Calibri",20),width=20)
        #entry5.grid(row=4,column=1)

        r1=Radiobutton(frameleft,text="male",font=("Calibri",20),value='male',variable=self.Patient_gender)
        r1.grid(row=4,column=1)
        
        r2=Radiobutton(frameleft,text="female",font=("Calibri",20),value='female',variable=self.Patient_gender)
        r2.grid(row=5,column=1)
        
        r1=Radiobutton(frameleft,text="others",font=("Calibri",20),value='others',variable=self.Patient_gender)
        r1.grid(row=6,column=1)


        entry6=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_address)
        entry6.grid(row=0,column=3)

        entry7=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_email)
        entry7.grid(row=1,column=3)

        entry8=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_phoneno)
        entry8.grid(row=2,column=3)

        entry9=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_adhaarno)
        entry9.grid(row=3,column=3)

        entry10=Entry(frameleft,font=("Calibri",20),width=20,textvariable=self.Patient_bloodgroup)
        entry10.grid(row=4,column=3)

        #button
        Button1=Button(buttonframe,text="view",bg="grey",fg="white",font=("Calibri",20,"bold"),width=15,command=self.viewvalues)
        Button1.grid(row=0,column=0)

        Button2=Button(buttonframe,text="insert",bg="grey",fg="white",font=("Calibri",20,"bold"),width=15,command=self.insertvalues)
        Button2.grid(row=0,column=1)

        Button3=Button(buttonframe,text="update",bg="grey",fg="white",font=("Calibri",20,"bold"),width=15,command=self.updatevalues)
        Button3.grid(row=0,column=2)

        Button4=Button(buttonframe,text="delete",bg="grey",fg="white",font=("Calibri",20,"bold"),width=15,command=self.deletevalues)
        Button4.grid(row=0,column=3)
        
        Button5=Button(buttonframe,text="clear",bg="grey",fg="white",font=("Calibri",20,"bold"),width=15,command=self.clearvalues)
        Button5.grid(row=0,column=4)
        

        Button6=Button(buttonframe,text="exit",bg="grey",fg="white",font=("Calibri",20,"bold"),width=16,command=messagebox1)
        Button6.grid(row=0,column=5)

        #textbox in viewbox
        self.txt=Text(viewframe,font=("Calibri",10,"bold"),width=45,height=17,padx=4,pady=6)
        self.txt.grid(row=0,column=0)

        #searchbox
        server = 'd2mtrainingdb.database.windows.net'
        db = 'd2manalysistraining'
        user = 'dbtuser'
        pwd = 'Disys@2022'
        conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
        cursor = conn.cursor()
        cursor.execute("select Patient_id from sk_patient_profile")
        row2=cursor.fetchall()
        list1=[]
        for x in row2:
            list1.append(x[0])
        cursor.close()    
        
        
        label11=Label(frameleft,text="Enter Patient_id",font=("Calibri",10,"bold"))
        label11.grid(row=5,column=2)
        button7=Button(frameleft,text='search',font=("calibri",10,"bold"),bg="grey",fg="white",command=self.searchdetails)
        button7.grid(row=6,column=3)
        tup=tuple(list1)
        dropbox=ttk.Combobox(frameleft,font=("Calibri",10,"bold"),width=20,textvariable=self.Patient_id)
        dropbox['values']=tup
        dropbox.grid(row=5,column=3)
        dropbox.current()

        #subframe3 scroll box
        scroll_x=ttk.Scrollbar(Detailframe,orient='horizontal')
        scroll_y=ttk.Scrollbar(Detailframe,orient='vertical')
        
        self.sk_patient_profile=ttk.Treeview(Detailframe,column=("Patient_id","Patient_name","Patient_age","Patient_dob","Patient_gender","Patient_address","Patient_email",
                                                                 "Patient_phoneno","Patient_adhaarno","Patient_bloodgroup"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)                                                       
        scroll_x=ttk.Scrollbar(command=self.sk_patient_profile.xview)
        scroll_y=ttk.Scrollbar(command=self.sk_patient_profile.yview)

        self.sk_patient_profile.heading("Patient_id",text="Patient id")
        self.sk_patient_profile.heading("Patient_name",text="Patient name")
        self.sk_patient_profile.heading("Patient_age",text="Patient age")
        self.sk_patient_profile.heading("Patient_dob",text="Patient dob")
        self.sk_patient_profile.heading("Patient_gender",text="Patient gender")
        self.sk_patient_profile.heading("Patient_address",text="Patient address")
        self.sk_patient_profile.heading("Patient_email",text="Patient email")
        self.sk_patient_profile.heading("Patient_phoneno",text="Patient phoneno")
        self.sk_patient_profile.heading("Patient_adhaarno",text="Patient adhaarno")
        self.sk_patient_profile.heading("Patient_bloodgroup",text="Patient bloodgroup")
        self.sk_patient_profile['show']="headings"

        self.sk_patient_profile.column("Patient_id",width=50)
        self.sk_patient_profile.column("Patient_name",width=50)
        self.sk_patient_profile.column("Patient_age",width=50)
        self.sk_patient_profile.column("Patient_dob",width=50)
        self.sk_patient_profile.column("Patient_gender",width=50)
        self.sk_patient_profile.column("Patient_address",width=50)
        self.sk_patient_profile.column("Patient_email",width=50)
        self.sk_patient_profile.column("Patient_phoneno",width=50)
        self.sk_patient_profile.column("Patient_adhaarno",width=50)
        self.sk_patient_profile.column("Patient_bloodgroup",width=50)
        self.sk_patient_profile.pack(fill=BOTH,expand=1)
        self.sk_patient_profile.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchingdata()
    def searchdetails(self):
        
        server = 'd2mtrainingdb.database.windows.net'
        db = 'd2manalysistraining'
        user = 'dbtuser'
        pwd = 'Disys@2022'
        conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
        cursor = conn.cursor()
        s1=self.Patient_id.get()
        cursor.execute("select * from sk_patient_profile where Patient_id=?",(s1,))
        a=cursor.fetchall()
        cursor.commit()
        self.Patient_id=a[0][0]
        self.Patient_name=a[0][1]                                                                                     
        self.Patient_age=a[0][2]
        self.Patient_dob=a[0][3]
        self.Patient_gender=a[0][4]
        self.Patient_address=a[0][5]
        self.Patient_email=a[0][6]
        self.Patient_phoneno=a[0][7]
        self.Patient_adhaarno=a[0][8]
        self.Patient_bloodgroup=a[0][9]
        root2=Tk()
        root2.geometry('500x500')
        label1=Label(root2,text="Patient id",font=("Calibri",20),padx=2)
        label1.grid(row=0,column=0,sticky="w")

        label2=Label(root2,text="Patient name",font=("Calibri",20),padx=2)
        label2.grid(row=1,column=0,sticky="w")

        label3=Label(root2,text="Patient age",font=("Calibri",20),padx=2)
        label3.grid(row=2,column=0,sticky="w")

        label4=Label(root2,text="Patient dob",font=("Calibri",20),padx=2)
        label4.grid(row=3,column=0,sticky="w")

        label5=Label(root2,text="Patient gender",font=("Calibri",20),padx=2)
        label5.grid(row=4,column=0,sticky="w")

        label6=Label(root2,text="Patient address",font=("Calibri",20),padx=2)
        label6.grid(row=5,column=0,sticky="w")

        label7=Label(root2,text="Patient email",font=("Calibri",20),padx=2)
        label7.grid(row=6,column=0,sticky="w")

        label8=Label(root2,text="Patient phoneno",font=("Calibri",20),padx=2)
        label8.grid(row=7,column=0,sticky="w")

        label9=Label(root2,text="Patient adhaarno",font=("Calibri",20),padx=2)
        label9.grid(row=8,column=0,sticky="w")

        label10=Label(root2,text="Patient bloodgroup",font=("Calibri",20),padx=2)
        label10.grid(row=9,column=0,sticky="w")
        

            
        
        
        
        
    def insertvalues(self):
        if len(self.Patient_phoneno.get())<10 and len(self.Patient_adhaarno.get())<12:
            print("check phoneno or adhaarno column")
        else:
            server = 'd2mtrainingdb.database.windows.net'
            db = 'd2manalysistraining'
            user = 'dbtuser'
            pwd = 'Disys@2022'
            conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
            s1=self.Patient_id.get()
            s2=self.Patient_name.get()                                                                                        
            s3=self.Patient_age.get()
            s4=self.Patient_dob.get()
            s5=self.Patient_gender.get()
            s6=self.Patient_address.get()
            s7=self.Patient_email.get()
            s8=self.Patient_phoneno.get()
            s9=self.Patient_adhaarno.get()
            s10=self.Patient_bloodgroup.get()

            

            cursor = conn.cursor()
            cursor.execute("insert into sk_patient_profile(Patient_id,Patient_name,Patient_age,Patient_dob,Patient_gender,Patient_address,Patient_email,Patient_phoneno,Patient_adhaarno,Patient_bloodgroup)values(?,?,?,?,?,?,?,?,?,?)",(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10))

            conn.commit()
            self.fetchingdata()
            conn.close()
            messagebox.showinfo("Box1","Record inserted")
    def fetchingdata(self):
        server = 'd2mtrainingdb.database.windows.net'
        db = 'd2manalysistraining'
        user = 'dbtuser'
        pwd = 'Disys@2022'
        conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
        cursor = conn.cursor()
        cursor.execute("select * from sk_patient_profile")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.sk_patient_profile.delete(*self.sk_patient_profile.get_children())
            for i in rows:
                self.sk_patient_profile.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.sk_patient_profile.focus()
        content=self.sk_patient_profile.item(cursor_row)
        row=content["values"]
        self.Patient_id.set(row[0])
        self.Patient_name.set(row[1])                                                                                        
        self.Patient_age.set(row[2])
        self.Patient_dob.set(row[3])
        self.Patient_gender.set(row[4])
        self.Patient_address.set(row[5])
        self.Patient_email.set(row[6])
        self.Patient_phoneno.set(row[7])
        self.Patient_adhaarno.set(row[8])
        self.Patient_bloodgroup.set(row[9])
        
        
        
    def updatevalues(self):
        
        server = 'd2mtrainingdb.database.windows.net'
        db = 'd2manalysistraining'
        user = 'dbtuser'
        pwd = 'Disys@2022'
        conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
        s1=self.Patient_id.get()
        s2=self.Patient_name.get()                                                                                        
        s3=self.Patient_age.get()
        s4=self.Patient_dob.get()
        s5=self.Patient_gender.get()
        s6=self.Patient_address.get()
        s7=self.Patient_email.get()
        s8=self.Patient_phoneno.get()
        s9=self.Patient_adhaarno.get()
        s10=self.Patient_bloodgroup.get()
        
        cursor = conn.cursor()
        
        
        cursor.execute("update sk_patient_profile set Patient_name=?,Patient_age=?,Patient_dob=?,Patient_gender=?,Patient_address=?,Patient_email=?,Patient_phoneno=?,Patient_adhaarno=?,Patient_bloodgroup=? where Patient_id=? ",s2,s3,s4,s5,s6,s7,s8,s9,s10,s1)
        conn.commit()
        conn.close()
        messagebox.showinfo("Box2","Record updated")
        
    
    def search_patient_details(self):
        server = 'd2mtrainingdb.database.windows.net'
        db = 'd2manalysistraining'
        user = 'dbtuser'
        pwd = 'Disys@2022'
        conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
        cursor = conn.cursor()
        s1=self.Patient_id.get()
        qry="select * from sk_patient_profile"
        val=s1
        cursor.execute(qry,val)
        conn.commit()
        conn.close()
    def viewvalues(self):
        
        s1=self.Patient_id.get()
        s2=self.Patient_name.get()                                                                                        
        s3=self.Patient_age.get()
        s4=self.Patient_dob.get()
        s5=self.Patient_gender.get()
        s6=self.Patient_address.get()
        s7=self.Patient_email.get()
        s8=self.Patient_phoneno.get()
        s9=self.Patient_adhaarno.get()
        s10=self.Patient_bloodgroup.get()
        self.txt.insert(END,"Patient id:\t\t" + s1 +"\n")
        self.txt.insert(END,"Patient name:\t\t" + s2 +"\n")
        self.txt.insert(END,"Patient age:\t\t" + s3 +"\n")
        self.txt.insert(END,"Patient dob:\t\t" + s4 +"\n")
        self.txt.insert(END,"Patient gender:\t\t" + s5 +"\n")
        self.txt.insert(END,"Patient address:\t\t" + s6 +"\n")
        self.txt.insert(END,"Patient email:\t\t" + s7 +"\n")
        self.txt.insert(END,"Patient phoneno:\t\t" + s8 +"\n")
        self.txt.insert(END,"Patient adhaarno:\t\t" + s9 +"\n")
        self.txt.insert(END,"Patient bloodgroup:\t\t" + s10 +"\n")    
        
        
        
        
    def deletevalues(self):
        
        server = 'd2mtrainingdb.database.windows.net'
        db = 'd2manalysistraining'
        user = 'dbtuser'
        pwd = 'Disys@2022'
        conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                             ';DATABASE=' + db +
                              '; UID=' + user +
                            '; PWD=' + pwd +
                             ';Trusted_Connection=no')
        cursor = conn.cursor()
        s1=self.Patient_id.get()
        action="delete from sk_patient_profile where Patient_id=?"
        value=s1
        cursor.execute(action,value)
        conn.commit()
        conn.close()
        messagebox.showinfo("Box3","Record Deleted")

        
    def clearvalues(self):
        
        self.Patient_id.set("")
        self.Patient_name.set("")                                                                                        
        self.Patient_age.set("")
        self.Patient_dob.set("")
        self.Patient_gender.set("")
        self.Patient_address.set("")
        self.Patient_email.set("")
        self.Patient_phoneno.set("")
        self.Patient_adhaarno.set("")
        self.Patient_bloodgroup.set("")

def messagebox1():
    toplevel=Toplevel(root)
    toplevel.title("QUITBOX")
    toplevel.geometry("300x300")
    
    l1=Label(toplevel,image="::tk::icons::warning")
    l1.grid(row=0,column=0)
    
    l2=Label(toplevel,text="Are you sure you want to quit")
    l2.grid(row=0,column=1)

    b1=Button(toplevel,text="yes",command=root.destroy,width=10)
    b1.grid(row=1,column=1)

    b2=Button(toplevel,text="no",command=toplevel.destroy,width=10)
    b2.grid(row=1,column=2)




root= Tk()
obj=hospital(root)
root.mainloop()
        
        

        


        

        

        


        

        
