print("hello")

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("STUDENT MANAGMENT SYSTEM")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        

        #1st
        img=Image.open(r"colleges_images\8th.jpg")
        img=img.resize((450,160),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,command=self.open_img,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=450,height=160)


        #2nd
        img_2=Image.open(r"colleges_images\2nd.jpg")
        img_2=img_2.resize((450,160),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=450,y=0,width=450,height=160)



        #3rd
        img_3=Image.open(r"colleges_images\3rd.jpg")
        img_3=img_3.resize((450,160),Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=900,y=0,width=450,height=160)


        #bg image
        img_4=Image.open(r"colleges_images\4th.jpg")
        img_4=img_4.resize((1350,610),Image.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1350,height=710)


        #label title
        lbl_title=Label(bg_lbl,text="STUDENT MANAGMENT SYSTEM",font=("Helvetica",37,"bold"),fg="red")
        lbl_title.place(x=1,y=1,width=1366,height=45)
        

        #manage Frame
        Manage_frame=Frame(bg_lbl,bd=4,relief=RIDGE,bg="white")
        Manage_frame.place(x=20,y=45,width=1300,height=500)
        

        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("Helvetica",25,"bold"),fg="navy blue",bg="white")
        DataLeftFrame.place(x=10,y=5,width=570,height=472)

        #img
        img_10=Image.open(r"colleges_images\71th.jpg")
        img_10=img_10.resize((550,710),Image.LANCZOS)
        self.photoimg_10=ImageTk.PhotoImage(img_10)

        my_img=Label(DataLeftFrame,image=self.photoimg_10,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=550,height=310)

        #current course labelFrame information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("Helvetica 9 italic",15,"bold","italic"),fg="navy blue",bg="white")
        std_lbl_info_frame.place(x=0,y=100,width=550,height=100)


        #Labels and combobox
        #department
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("Helvetica",13,"bold"),fg="red",bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",10),width=15,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=5)

        #course
        course_std=Label(std_lbl_info_frame,text="Course",font=("Helvetica",13,"bold"),fg="red",bg="white")
        course_std.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        combo_course_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=("arial",10),width=15,state="readonly")
        combo_course_std["value"]=("Select Course","EE","SE","TE","BE")
        combo_course_std.current(0)
        combo_course_std.grid(row=0,column=3,sticky=W,padx=2,pady=5)


        #year
        current_year=Label(std_lbl_info_frame,text="Year",font=("Helvetica",13,"bold"),fg="red",bg="white")
        current_year.grid(row=1,column=0,padx=2,pady=3,sticky=W)
  
        combo_current_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("arial",10),width=15,state="readonly")
        combo_current_year["value"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        combo_current_year.current(0)
        combo_current_year.grid(row=1,column=1,padx=2,pady=3)

        #semester
        label_semester=Label(std_lbl_info_frame,text="Semester",font=("Helvetica",13,"bold"),fg="red",bg="white")
        label_semester.grid(row=1,column=2,padx=2,pady=3,sticky=W)

        combo_semester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester,font=("arial",10),width=15,state="readonly")
        combo_semester["value"]=("Select Semester","1st","2nd","3rd","4th")
        combo_semester.current(0)
        combo_semester.grid(row=1,column=3,padx=2,pady=3)


   
        #class course information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("Helvetica",15,"bold","italic"),fg="navy blue",bg="white")
        std_lbl_class_frame.place(x=0,y=205,width=550,height=190)
        
        #labels entry
        #ID
        label_id=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Student Id:",fg="red",bg="white")
        label_id.grid(row=0,column=0,padx=1,pady=2,sticky=W)
        
        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("Helvetica",12,"bold"),width=15)
        id_entry.grid(row=0,column=1,padx=5,pady=2,sticky=W)

        
        #Name   
        label_Name=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Student Name:",fg="red",bg="white")
        label_Name.grid(row=0,column=2,padx=1,pady=2,sticky=W)
        
        txt_name=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name,font=("Helvetica",12,"bold"),width=15)
        txt_name.grid(row=0,column=3,padx=1,pady=2,sticky=W)

        #Division
        label_div=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Division:",fg="red",bg="white")
        label_div.grid(row=1,column=0,padx=2,pady=1,sticky=W)
        
        txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,font=("Helvetica",10),width=15)
        txt_div["value"]=("Select Division","A","A+","B","B+","C","Fail")
        txt_div.current(0)
        txt_div.grid(row=1,column=1,padx=4,pady=2,sticky=W)
        txt_div.config(width=17)
        
        #Roll
        label_roll=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Roll No:",fg="red",bg="white")
        label_roll.grid(row=1,column=2,padx=1,pady=2,sticky=W)
        
        txt_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=("Helvetica",12,"bold"),width=15)
        txt_roll.grid(row=1,column=3,padx=1,pady=2,sticky=W)


        

        #gender
        label_gender=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Gender:",fg="red",bg="white")
        label_gender.grid(row=2,column=0,padx=1,pady=2,sticky=W)
        
        txt_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,font=("Helvetica",10),width=15)
        txt_gender['value']=("Select Gender","male","female","other")
        txt_gender.current(0)
        txt_gender.grid(row=2,column=1,padx=4,pady=1,sticky=W)
        txt_gender.config(width=17)

        #DOB
        label_dob=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Dob:",fg="red",bg="white")
        label_dob.grid(row=2,column=2,padx=1,pady=2,sticky=W)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,font=("Helvetica",12,"bold"),width=15)
        txt_dob.grid(row=2,column=3,padx=1,pady=2,sticky=W)

        #Email
        label_dob=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Email:",fg="red",bg="white")
        label_dob.grid(row=3,column=0,padx=1,pady=2,sticky=W)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("Helvetica",12,"bold"),width=15)
        txt_dob.grid(row=3,column=1,padx=1,pady=2,sticky=W)

        #phone
        label_phone=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Phone:",fg="red",bg="white")
        label_phone.grid(row=3,column=2,padx=1,pady=2,sticky=W)
        
        txt_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,font=("Helvetica",12,"bold"),width=15)
        txt_phone.grid(row=3,column=3,padx=1,pady=2,sticky=W)


        #address
        label_address=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Address:",fg="red",bg="white")
        label_address.grid(row=4,column=0,padx=1,pady=2,sticky=W)
        
        txt_address=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,font=("Helvetica",12,"bold"),width=15)
        txt_address.grid(row=4,column=1,padx=1,pady=2,sticky=W)


        #Teacher
        label_teacher=Label(std_lbl_class_frame,font=("Helvetica",12,"bold"),text="Teacher Name:",fg="red",bg="white")
        label_teacher.grid(row=4,column=2,padx=1,pady=2,sticky=W)
        
        txt_teacher=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher,font=("Helvetica",12,"bold"),width=15)
        txt_teacher.grid(row=4,column=3,padx=1,pady=2,sticky=W)
        
        #Button Frame
        btn_frame=Frame(DataLeftFrame,bd=4,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=395,width=552,height=30)

        btn_Add=Button(btn_frame,text="save",command=self.add_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=0)

        btn_Update=Button(btn_frame,text="update",command=self.update_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_Update.grid(row=0,column=1,padx=1)
        
        btn_Delete=Button(btn_frame,text="delete",command=self.delete_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_Delete.grid(row=0,column=2,padx=1)
        
        btn_Reset=Button(btn_frame,text="reset",command=self.reset_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_Reset.grid(row=0,column=3,padx=1)


        #Right frame                                                                                                                                                                                                                                                                                                                                    
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("Helvetica",10,"bold"),fg="navy blue",bg="white")
        DataRightFrame.place(x=580,y=5,width=700,height=472)
        #img
        img_5=Image.open(r"colleges_images\1st.jpg")
        img_5=img_5.resize((685,710),Image.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(DataRightFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=685,height=100)

        # Search right frame                                                                                                                                                                                                                                                                                                                                    
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search student information",font=("Helvetica",10,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=100,width=685,height=60)

        #search by
        Search_by=Label(Search_Frame,font=("Helvetica",10,"bold"),text="Search By",fg="white",bg="navy blue")
        Search_by.grid(row=0,column=0,padx=1,pady=0,sticky=W)

        #search
        #combobox
        #select option
        self.var_com_search=StringVar()
        txt_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,font=("Helvetica",10),width=15)
        txt_search['values']=("Select Option","Roll","Phone","Student_Id")
        txt_search.current(0)
        txt_search.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        txt_search.config(width=15)
        
        #search
        #Entry
        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search,font=("Helvetica",10,"bold"),width=18)
        txt_search.grid(row=0,column=2,padx=5,sticky=W)

        #Button 
        #Search
        btn_search=Button(Search_Frame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=15,bg="navy blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        #showall
        btn_showAll=Button(Search_Frame,command=self.fetch_data,text="Show All Records",font=("arial",11,"bold"),width=15,bg="navy blue",fg="white")
        btn_showAll.grid(row=0,column=4,padx=5)


    


        #===============Student Table and scroll bar==================
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=160,width=685,height=290)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")

        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #save function
    def add_data(self):
        if (self.var_dep.get()=="" or self.var_course.get()=="" or self.var_year.get()==""):
        #or self.var_semester.get()=="" or self.var_id.get()=="" or  self.var_name.get()=="" or 
        #self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or
        #self.var_dob.get()==""or self.var_email.get()=="" or self.var_phone.get()=="" or 
        #self.var_address.get()==""or self.var_teacher.get()==""):
           messagebox.showerror("Error","ALL Fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root",password="abc123", database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_std_id.get(),
                                                self.var_std_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 



    #fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="abc123",database="my_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor in the entry field  
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        
    #update
    def update_data(self):
        if (self.var_dep.get()=="" or self.var_course.get()=="" or self.var_year.get()==""):
           messagebox.showerror("Error","ALL Fields are required") 
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="abc123",database="my_data")
                    my_cursor=conn.cursor()
                    sql = "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s"
                    val = ( self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_std_id.get()  )
                    my_cursor.execute(sql,val)
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("success","student successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    #delete               
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are sure delete this student",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="abc123",database="my_data")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","your student has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
    

    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("select course")
        self.var_course.set("select Year")
        self.var_semester.set("select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("error","please select option") 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="abc123",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #open image
    def open_img(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open images",filetypes=(("JPG File",".jpg"),("PNG File",".png"),("All files",".")))             
        img=Image.open(fln)
        img_browse=img.resize((450,160),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
