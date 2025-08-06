import pymysql
import streamlit as st
import time

db=pymysql.connect(host='localhost',user='root',password='',database='parv')
cursor=db.cursor()


class SignUp:
  def __init__(self):
     with st.form(key="Sign_up_form",clear_on_submit=True):
      name=st.text_input(label="Name",placeholder="Enter your name: ")
      mobile_number=st.text_input(label="Mobile Number",placeholder="Enter your mobile number: ")
      email=st.text_input(label="Email",placeholder="Enter your email: ")
      col1,col2=st.columns(2,gap='medium')
      with col1:
        username=st.text_input(label="Username",placeholder="Enter your username: ")
      with col2:
        password=st.text_input(label="Password",placeholder="Enter your password: ",type='password')
      sign_up_button=st.form_submit_button(label="Sign Up",use_container_width=True)
      if sign_up_button:
        self.Validate(name,mobile_number,email,username,password)

  def Validate(self,name,mobile_number,email,username,password):
    if not(name) or not(mobile_number) or not(email) or not(username) or not(password):
      st.error("Please fill out the details")
      return
    if len(mobile_number)!=10 or not(mobile_number.isdigit()):
      st.error("Please enter appropriate mobile number")
      return
    if username==password:
      st.error("Username and password cannot be the same")
      return
    
    sign_up_query="INSERT into signup(NAME,USER_NAME,MOBILE_NO,EMAIL_ID,PASSWORD) values(%s,%s,%s,%s,%s)"
    try:
      cursor.execute(sign_up_query,(name,username,mobile_number,email,password))
      result=cursor.rowcount
      if result:
        st.success("SIGN UP SUCCESFULL")
        db.commit()
        st.info("redirecting you to the login page")
        progress=st.progress(0)
        for i in range(100):
          time.sleep(0.02)
          progress.progress(i+1)
          st.switch_page(page='main.py')
      else:
        st.error("There was a problem signing up")
        db.rollback()
    except Exception as e:
      st.error(f"There was an error: {e}")
      db.rollback()


s=SignUp()



