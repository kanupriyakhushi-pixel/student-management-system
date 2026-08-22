# Student Management System

A command-line based **Student Management System built using Python and MySQL**.

This project started as a basic Python file-handling application and was upgraded into a database-backed application using `mysql-connector-python`. It allows users to manage student records, store marks, and generate different academic performance reports directly from a MySQL database.

## 🚀 Features

### 👩‍🎓 Student Management

* Add new students
* Search students by name
* Remove students using student ID
* Display all students
* Store student information permanently in MySQL

### 📚 Marks Management

* Add marks for students
* Display all marks
* View individual student marks
* Store marks subject-wise

### 📊 Performance Reports

* Student performance report
* Calculate total marks
* Calculate average marks
* Find the top-performing student
* Find students who scored below 40
* Course-wise performance
* Subject-wise performance
* Student-specific performance
* Student ranking based on average marks

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **mysql-connector-python**
* SQL
* Git & GitHub

## 🧠 Concepts Learned

### Python

* Variables and data types
* Input/output
* Conditional statements
* Loops
* Functions
* Exception handling
* Working with external libraries

### MySQL / SQL

* Database creation
* Table creation
* Primary keys
* Foreign keys
* `INSERT`
* `SELECT`
* `DELETE`
* `WHERE`
* `INNER JOIN`
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `LIMIT`
* Aggregate functions:

  * `SUM()`
  * `AVG()`

### Python + MySQL Integration

* Connecting Python to MySQL
* Creating a MySQL cursor
* Executing SQL queries from Python
* Passing values safely using placeholders
* Using `fetchall()`
* Committing database changes with `commit()`
* Closing the database connection

## 🗄️ Database Structure

The project uses a MySQL database called:

```text
student_management
```

### `students` table

| Column       | Description              |
| ------------ | ------------------------ |
| `student_id` | Unique ID of the student |
| `name`       | Student name             |
| `course`     | Student's course         |
| `year`       | Student's academic year  |

### `marks` table

| Column       | Description                     |
| ------------ | ------------------------------- |
| `mark_id`    | Unique ID for each marks record |
| `student_id` | ID of the student               |
| `subject`    | Subject name                    |
| `marks`      | Marks obtained                  |

The `student_id` in the `marks` table is connected to the `students` table using a **foreign key**.

```text
students
   │
   │ student_id
   ↓
marks
```

## 📂 Project Structure

```text
student_management/
│
├── student_management.py    # Main Python application
├── marks.py                 # Earlier marks-management module
├── student_management.sql   # Database and sample data
├── students.txt             # Old file-based storage (initial version)
├── README.md
└── .gitignore
```

> `marks.py` was used while developing and learning the marks-management functionality. The final application integrates the marks functionality into `student_management.py`.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd student-management-system
```

### 3. Install MySQL Connector

```bash
pip install mysql-connector-python
```

### 4. Set up MySQL

Open MySQL Workbench and run the SQL commands from:

```text
student_management.sql
```

This creates the database, tables, and sample records.

### 5. Configure the database connection

The Python application requires:

```text
Host: localhost
User: root
Database: student_management
```

**Do not publish your actual MySQL password on GitHub.**

For a public repository, store the password using environment variables and keep the `.env` file out of Git.

### 6. Run the application

```bash
python student_management.py
```

## 📋 Main Menu

```text
==========================STUDENT MANAGEMENT SYSTEM==========================

1. Add Student
2. Search Student
3. Remove Student
4. Display Students
5. Add Marks
6. Display All Marks
7. Student Performance
8. Top Performer
9. Failed Students
10. Course-wise Performance
11. Student-specific Performance
12. Student Ranking
13. Subject-wise Performance
14. Exit
```

## 📊 Example Reports

### Student Performance

```text
Student       Total Marks       Average Marks
Kanupriya     323               80.75
Aarav         351               87.75
Rohan         368               92.00
```

### Top Performer

```text
==========================TOP PERFORMER==========================

Rohan
Average Marks: 92.00
```

### Subject-wise Performance

```text
==========================SUBJECT WISE PERFORMANCE==========================

DBMS       82.50
Python     86.30
CS         70.80
DSA        80.40
Maths      31.00
```

## 🔐 Security Note

Database credentials should **never be committed to GitHub**.

Use environment variables for sensitive information such as:

```text
DB_HOST
DB_USER
DB_PASSWORD
DB_NAME
```

Add the following to `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

## 🔮 Future Improvements

Possible future improvements include:

* Input validation for marks between 0 and 100
* Better exception handling for database errors
* Automatic `mark_id` generation using `AUTO_INCREMENT`
* Improved terminal formatting
* Admin/user authentication
* GUI using Tkinter
* Web application using Flask
* Export performance reports to CSV
* Data visualization using Python
* Student attendance management

## 🎓 Project Learning Outcome

This project helped me move from a basic Python file-handling application to a **database-backed application**.

The project demonstrates how Python can communicate with MySQL to perform CRUD operations and execute analytical SQL queries for generating meaningful student performance reports.

## 👩‍💻 Author

**Kanupriya Upadhyay**

B.Tech Artificial Intelligence & Data Science Student

Interested in Python, Data Analytics, Machine Learning and AI.

---

⭐ This project was built as part of my journey of learning Python, SQL, and database integration.
