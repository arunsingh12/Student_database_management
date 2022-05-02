from tkinter import *
from tkinter import ttk
import pymysql


class student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student management system")
		self.root.geometry("1350x700+0+0")

		title=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bd=10,relief=GROOVE,bg="blue",fg="white")
		title.pack(side=TOP,fill=X)

		#=======================All Variables========

		self.roll_No_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.gender_var=StringVar()
		self.contact_var=StringVar()
		self.dob_var=StringVar()

		self.search_by=StringVar()
		self.search_txt=StringVar()

############----- manage frame----####

		Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
		Manage_frame.place(x=20,y=100,width=450,height=580)

		m_title=Label(Manage_frame,text="Manage Students",bg="blue",fg="white",font=("times new roman",20,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)

		lbl_roll=Label(Manage_frame,text="Roll No.-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		txt_Roll=Entry(Manage_frame,textvariable=self.roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_Roll.grid(row=1,column=1,padx=20,sticky="w")

		lbl_name=Label(Manage_frame,text="Name-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		txt_name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_name.grid(row=2,column=1,padx=20,sticky="w")

		lbl_Email=Label(Manage_frame,text="Email-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		txt_Email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_Email.grid(row=3,column=1,padx=20,sticky="w")

		lbl_Gender=Label(Manage_frame,text="Gender-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state="readonly")
		combo_gender['values']=("male","female","other")
		combo_gender.grid(row="4",column="1",pady="10",padx="20")



		lbl_Contact=Label(Manage_frame,text="Contact-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		txt_Contact=Entry(Manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_Contact.grid(row=5,column=1,padx=20,sticky="w")


		lbl_DOB=Label(Manage_frame,text="D.O.B.-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

		txt_DOB=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
		txt_DOB.grid(row=6,column=1,padx=20,sticky="w")

		lbl_Address=Label(Manage_frame,text="Address-",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

		self.txt_Address=Text(Manage_frame,width=30,height=4,font=("",10))
		self.txt_Address.grid(row=7,column=1,padx=20,pady=10,sticky="w")



		#========Button Frame=======#
		Btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="blue")
		Btn_frame.place(x=10,y=500,width=420)
		Addbtn=Button(Btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
		Updatebtn=Button(Btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
		Deletebtn=Button(Btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
		Clearbtn=Button(Btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

#################### Detail frame###

		Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
		Detail_frame.place(x=500,y=100,width=800,height=580)

		lbl_Search=Label(Detail_frame,text="Search_By",bg="blue",fg="white",font=("times new roman",20,"bold"))
		lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

		combo_Search=ttk.Combobox(Detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
		combo_Search['values']=("Roll_no","Name","Contact")
		combo_Search.grid(row=0,column=1,pady="10",padx="20")

		txt_Search=Entry(Detail_frame,textvariable=self.search_txt,width=15,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
		txt_Search.grid(row=0,column=2,padx=20,pady=10,sticky="w")



		searchbtn=Button(Detail_frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
		showalldbtn=Button(Detail_frame,text="Showall",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

		#========Table Frame========
		Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="blue")
		Table_frame.place(x=10,y=70,width=760,height=500)

		scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
		self.Student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading("roll",text="Roll No.")
		self.Student_table.heading("name",text="Name")
		self.Student_table.heading("email",text="Email")
		self.Student_table.heading("gender",text="Gender")
		self.Student_table.heading("contact",text="Contact")
		self.Student_table.heading("dob",text="D.O.B.")
		self.Student_table.heading("address",text="Address")
		self.Student_table['show']='headings'

		self.Student_table.column("roll",width=100)
		self.Student_table.column("name",width=100)
		self.Student_table.column("email",width=100)
		self.Student_table.column("gender",width=100)
		self.Student_table.column("contact",width=100)
		self.Student_table.column("dob",width=100)
		self.Student_table.column("address",width=150)

		self.Student_table.pack(fill=BOTH,expand=1)
		self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()

	def add_students(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_No_var.get(),
																		self.name_var.get(),
																		self.email_var.get(),
																		self.gender_var.get(),
																		self.contact_var.get(),
																		self.dob_var.get(),
																		self.txt_Address.get('1.0',END)
																			))

		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def fetch_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("select * from students")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()

	def clear(self):
		self.roll_No_var.set("")
		self.name_var.set("")
		self.email_var.set("")
		self.gender_var.set("")
		self.contact_var.set("")
		self.dob_var.set("")
		self.txt_Address.delete("1.0",END)


	def get_cursor(self,ev):
		cursor_row=self.Student_table.focus()
		contents=self.Student_table.item(cursor_row)
		row=contents['values']
		self.roll_No_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.contact_var.set(row[4])
		self.dob_var.set(row[5])
		self.txt_Address.delete("1.0",END)
		self.txt_Address.insert(END,row[6])


	def update_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
																		self.name_var.get(),
																		self.email_var.get(),
																		self.gender_var.get(),
																		self.contact_var.get(),
																		self.dob_var.get(),
																		self.txt_Address.get('1.0',END),
																		self.roll_No_var.get()
																			))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()


	def delete_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("delete from students where roll_no=%s",self.roll_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()


	def search_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="stm")
		cur=con.cursor()
		cur.execute("select * from students where"+str(self.search_by.get())+"LIKE '%"+str(self.search_txt.get())+"%'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()

root=Tk()
ob=student(root)
root.mainloop()
