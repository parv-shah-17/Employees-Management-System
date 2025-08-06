import pymysql
import streamlit as st

db=pymysql.connect(host='localhost',user='root',password='',database='parv')
cursor=db.cursor()

st.title("My Dashboard",anchor=False)

add = st.button(label= "Add Employee", use_container_width=True)
if add:
    st.switch_page(page='pages/add.py')

delete = st.button(label= "Delete Employee", use_container_width=True)
if delete:
    st.switch_page(page='pages/delete.py')

view = st.button(label= "View Employee", use_container_width=True)
if view:
    st.switch_page(page='pages/view.py')

logOut = st.button(label= "LogOut", use_container_width=True)
if logOut:
    st.switch_page(page='main.py')











