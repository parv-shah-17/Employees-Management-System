import pymysql
import streamlit as st

db = pymysql.connect(host='localhost', user='root', password='', database='parv')
cursor = db.cursor()

def main():
    st.title("Search Employee by Name")
    
    name = st.text_input("Enter Full Name", placeholder="e.g., John Dae")

    if st.button("Search"):
        try:
            query = "SELECT * FROM employees WHERE NAME = %s"
            cursor.execute(query, (name,))
            result = cursor.fetchone()  

            if result:
                columns = [desc[0] for desc in cursor.description]

                st.subheader("Employee Information")
                for col, val in zip(columns, result):
                    st.write(f"**{col}**: {val}")
            else:
                st.warning("No employee found with that name.")

        except Exception as e:
            st.error(f"An error occurred: {e}")


main()
