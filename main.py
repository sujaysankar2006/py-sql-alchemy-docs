import curd
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def employee_operations():
    db = SessionLocal()
    
 
    print('EMPLOYEE MANAGEMENT SYSTEM')
    print('1. Create new employee')
    print('2. Get employee by name')
    print('3. Update employee age')     
    print('4. Update employee department')
    print('5. Delete employee by name')
    
    choice = int(input('Enter your choice: '))

    # -------------------------------
    # 1. CREATE EMPLOYEE
    # -------------------------------
    if choice == 1:
        name = input('Enter employee name: ')
        age = int(input('Enter employee age: '))
        department_id = int(input('Enter department ID: '))

        result = curd.create_new_employee(db, name, age, department_id)
        print(f"Employee created: ")

    # -------------------------------
    # 2. GET EMPLOYEE
    # -------------------------------
    elif choice == 2:
        name = input('Enter employee name to get details: ')
        employee = curd.get_employee_by_name(db, name)
        if employee:
            print(f"Employee Details: ID={employee.id}, Name={employee.name}, Age={employee.age}, Department ID={employee.department_id}")
        else:
            print("Employee not found.")

    # -------------------------------
    # 3. UPDATE AGE
    # -------------------------------
    elif choice == 3:
        name = input('Enter employee name to update age: ')
        age = int(input('Enter new age: '))
        print(curd.update_employee_age(db, name, age))

    # -------------------------------
    # 4. UPDATE DEPARTMENT
    # -------------------------------
    elif choice == 4:
        name = input('Enter employee name to update department: ')
        department_id = int(input('Enter new department ID: '))
        print(curd.update_employee_department(db, name, department_id))

    # -------------------------------
    # 5. DELETE EMPLOYEE
    # -------------------------------
    elif choice == 5:
        name = input('Enter employee name to delete: ')
        print(curd.delete_employee_by_name(db, name))

    else:
        print('Invalid choice')


if __name__ == '__main__':
    employee_operations()
