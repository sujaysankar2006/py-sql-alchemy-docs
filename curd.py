from sqlalchemy.orm import Session
from models import Employee,Department
from database import engine,Base

Base.metadata.create_all(bind=engine)

#to create a new employee
def create_new_employee(db:Session,name:str,age:int,department_id:int):
    new_employee=Employee(name=name,age=age,department_id=department_id)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return f" new employee added sucessfully"


#to create a new department
def create_new_department(db:Session,name:str,id:int,location:str,head:str):
    new_department=Department(name=name,id=id,location=location,head=head)
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return f" new department added sucessfully"

#to get employee by name

def get_employee_by_name(db:Session,name:str):
    return db.query(Employee).filter(Employee.name==name).first()
 
# update employe age
def update_employee_age(db:Session,name:str,age:int):
    update_age_by_name=db.query(Employee).filter(Employee.name==name).first()
    if update_age_by_name:
          update_age_by_name.age=age
          db.commit()
          db.refresh(update_age_by_name)
          return f" employee age updated successfully :{age}"

def updating_employee_department(db:Session,name:str,department:str):
    update_department_by_name=db.query(Employee).filter(Employee.name==name).first()
    if update_department_by_name:
          update_department_by_name.department=department
          db.commit()
          db.refresh(update_department_by_name)
          return f" employee department updated successfully :{department}"

#deleting an employee
def delete_employee_by_name(db:Session,name:str):
    delete_employee=db.query(Employee).filter(Employee.name==name).first()
    if delete_employee:
          db.delete(delete_employee)
          db.commit()
          return f" employee deleted successfully :{name}"        