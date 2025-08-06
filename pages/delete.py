import pymysql
import streamlit as st

db = pymysql.connect(host='localhost', user='root', password='', database='parv')
cursor = db.cursor()

class Main:
    def __init__(self):
        self.show_form()

    def show_form(self):
        with st.form(key="Delete Employee", clear_on_submit=True):
            name = st.text_input(label="Name", placeholder="Enter Full Name to Delete")
            delete_employee = st.form_submit_button(label="Delete", use_container_width=True)

            if delete_employee:
                self.delete(name)

    def delete(self, name):
        try:
            query = "DELETE FROM employees WHERE NAME = %s"
            cursor.execute(query, (name,))
            db.commit()

            if cursor.rowcount > 0:
                st.success("Deleted SUCCESSFULLY")
            else:
                st.warning("No employee found with that name.")

        except Exception as e:
            st.error(f"Error occurred: {e}")

aa = Main()


