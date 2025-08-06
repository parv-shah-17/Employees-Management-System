import pymysql
import streamlit as st

db=pymysql.connect(host='localhost',user='root',password='',database='parv')
cursor=db.cursor()

class MainPanel:
  def __init__(self):  
    with st.form(key="login_form",clear_on_submit=True):
      username=st.text_input(label="Username",placeholder="Your username")
      password=st.text_input(label="Password",placeholder="Your Password",type='password')
      login_button=st.form_submit_button(label="LOGIN",use_container_width=True)
      if login_button:
        self.login(username,password)
    st.html("<H1 style='text-align: center;'>OR</H1>")
    sign_up_button=st.button(label="SIGN UP",use_container_width=True)
    
    
    if sign_up_button:
      st.switch_page(page='pages/sign_up_page.py')
      st.title("Hello world")
  
  
  
  
  def login(self,username,password):
    if username=="" or password=="" or username.isspace() or password.isspace():
      st.error("Please fill out appropriate details")
      return
    
    try:
      login_query="SELECT * FROM signup WHERE USER_NAME=%s and PASSWORD=%s"
      cursor.execute(login_query,(username,password))
      result=cursor.fetchone()
      if result:
        st.success("SUCCESFULLY LOGGED IN")
        db.commit()
        st.switch_page(page='pages/dashboard.py')
      else:
        st.error("INCORRECT USERNAME or PASSWORD")
        db.rollback()
    except Exception as e:
      st.error(f"There was an error {e}")
      db.rollback()




m=MainPanel()