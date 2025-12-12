from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__='employees'
    id=Column(Integer,unique=True,autoincrement=True,primary_key=True)
    name=Column(String,index=True)
    age=Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")
class Department(Base):
    __tablename__='departments'
    id=Column(Integer,unique=True,autoincrement=True,primary_key=True)
    name=Column(String,index=True)
    location=Column(String) 
    head=Column(String)
    employees = relationship("Employee", back_populates="department")
