import pymysql
import streamlit as st

db=pymysql.connect(host='localhost',user='root',password='',database='parv')
cursor=db.cursor()

class Main:
  def __init__(self):
   with st.form(key="Add Employee",clear_on_submit=True):
      Name=st.text_input(label="Name",placeholder="Enter Your Full Name")
      Mobile=st.text_input(label="Mobile",placeholder="Enter Mobile No.")
      Email=st.text_input(label="Email",placeholder="Enter Your Email")
      Post=st.text_input(label="Post",placeholder="Enter Your Post")
      Salary=st.text_input(label="Salary",placeholder="Enter Your Salary")
      add_employee=st.form_submit_button(label="Added",use_container_width=True)
      if add_employee:
        self.Add(Name, Mobile, Email, Post, Salary)
      

  def Add(self,Name, Mobile, Email, Post, Salary):
      Add_Employee_query="INSERT into employees(NAME, MOBILE_NO, EMAIL, POST, SALARY) values(%s,%s,%s,%s,%s)"
      cursor.execute(Add_Employee_query,(Name, Mobile, Email, Post, Salary))
      result=cursor.rowcount
      if result:
        st.success("SIGN UP SUCCESFULL")
        db.commit()
      else:
        print("Given Information is Incorrect")
        st.switch_page(page='pages/add.py')

aa = Main()



