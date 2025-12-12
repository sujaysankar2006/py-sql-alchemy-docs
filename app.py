import streamlit as st
from database import SessionLocal,engine,Base
import curd 
st.header("Employee Management System")
Base.metadata.create_all(bind=engine)
st.write("Welcome to the Employee Management System")
db=SessionLocal()
Menu=["Create New Employee","Get Employee by Name","Update Employee Age","Update Employee Department","Delete Employee by Name","all employees"]
choice=st.sidebar.selectbox("Menu",Menu)
if choice=="Create New Employee":
    st.subheader("Create New Employee")
    name=st.text_input("Enter Employee Name")
    age=st.number_input("Enter Employee Age",min_value=18,max_value=70,step=1)
    department_id=st.number_input("Enter Department ID",min_value=1,step=1)
    if st.button("Create Employee"):
        result=curd.create_new_employee(db,name,age,department_id)
        st.success(result)
elif choice=="Get Employee by Name":
    st.subheader("Get Employee by Name")
    name=st.text_input("Enter Employee Name to Get Details")
    if st.button("Get Employee"):
        employee=curd.get_employee_by_name(db,name)
        if employee:
            st.write(f"Employee Details: ID={employee.id}, Name={employee.name}, Age={employee.age}, Department ID={employee.department_id}")
        else:
            st.error("Employee not found.")
elif choice=="Update Employee Age":     
    st.subheader("Update Employee Age")
    name=st.text_input("Enter Employee Name to Update Age")
    age=st.number_input("Enter New Age",min_value=18,max_value=70,step=1)
    if st.button("Update Age"):
        result=curd.update_employee_age(db,name,age)
        st.success(result)
elif choice=="Update Employee Department":  
    st.subheader("Update Employee Department")
    name=st.text_input("Enter Employee Name to Update Department")
    department_id=st.number_input("Enter New Department ID",min_value=1,step=1)
    if st.button("Update Department"):
        result=curd.updating_employee_department(db,name,department_id)
        st.success(result)
elif choice=="Delete Employee by Name":
    st.subheader("Delete Employee by Name")
    name=st.text_input("Enter Employee Name to Delete")
    if st.button("Delete Employee"):
        result=curd.delete_employee_by_name(db,name)
        st.success(result)  
        st.success(f"Employee deleted: {name}")
elif choice=="all employees":
    st.subheader("All Employees")
    employees=db.query(curd.Employee).all()
    for emp in employees:
        st.write(f"ID={emp.id}, Name={emp.name}, Age={emp.age}, Department ID={emp.department_id}")
