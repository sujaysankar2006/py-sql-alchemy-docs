# SQLAlchemy Employee Management System  
A simple SQLAlchemy-based backend application that demonstrates:

- Database modeling (Departments & Employees)
- CRUD operations (Create, Read, Update, Delete)
- CLI-based employee management
- Streamlit-based interactive UI
- SQLite local database
- Python project structure (models, crud, database, UI)

---

## 📁 Project Structure
sqldocs/
│
├── database.py           # DB connection, engine, SessionLocal
├── models.py             # SQLAlchemy ORM models
├── curd.py               # CRUD functions for Department & Employee
├── main.py               # CLI-based employee management system
├── app.py                # Streamlit web UI
└── README.md
---

## 🛠 Technologies Used

- **Python 3**
- **SQLAlchemy ORM**
- **SQLite**
- **Streamlit**
- **CLI-based input system**

---

## 🚀 Features

### ✔ Employee Management  
- Add new employees  
- View employee details  
- Update employee age  
- Update employee department  
- Delete employee  

### ✔ Department Management  
- Add departments  
- Link employees to departments  
- Fetch employee’s department details  
- One-to-Many relationship

### ✔ Streamlit UI  
- Create Departments  
- Create Employees  
- View Employees list  
- Update/Delete operations  

---

## ⚙️ Installation

Make sure Python 3 is installed.

### 1. Clone the repository

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>'

2. Install dependencies
or manually:pip install sqlalchemy ,pip install streamlit

3. Running the CLI App
   python3 main.py
4.Running the Streamlit App
 python3 -m streamlit run app.py or streamlit run app.py
5. Example CLI Workflow
  EMPLOYEE MANAGEMENT SYSTEM
1. Create new employee
2. Get employee by name
3. Update employee age
4. Update employee department
5. Delete employee by name

   






