# 🎓 Relational Student Management System

An advanced, production-ready command-line Student Management System built using Python and backed by a MySQL relational database.

This project bridges the gap between software development and database engineering, moving away from temporary file storage to permanent, scalable data infrastructure.

## 🚀 Features

✅ **Persistent Storage:** Fully integrated with MySQL Server—records survive application restarts.
✅ **Relational Architecture:** Tracks unique Student records and Maps their performance metrics through a shared `student_id` relationship.
✅ **Analytical Computations:** Computes real-time data metrics including class averages, overall sums, student rankings, and core performance breakdowns using SQL aggregation functions.
✅ **Failing Alert System:** Instantly isolates and catches academic records failing to meet predefined score benchmarks (marks < 40).
✅ **Data Type Guardrails:** Implements comprehensive `try-except` wrappers to prevent script crashes on invalid numeric configurations.
✅ **SQL Leakage Prevention:** Built with secure, parameterised SQL script queries to eliminate risk exposures.

## 🛠️ Technologies & Packages Used

* **Python 3** (Application Engine)
* **MySQL Server** (Relational Database Data Tier)
* **mysql-connector-python** (Database Driver Linker)
* **python-dotenv** (Environment Configuration Security)
* **Git & GitHub** (Version Control Platform)

## 📂 New Project Structure

```text
student_management/
│
├── .env                          # Secure local environment variables (HIDDEN FROM GITHUB)
├── .gitignore                    # Restricts private credentials from uploading publically
├── student_management.py         # Main execution script and terminal menu system
├── marks.py                      # Data model logic handling academic scores
└── README.md                     # Documentation panel
```

## 🔐 Security Notice (.env setup)
To protect structural database access keys from leaking online, create a `.env` file inside your project root and configure it as follows before execution:
```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_SECRET_PASSWORD
DB_NAME=student_management
```

## ▶️ How to Setup & Run

### 1. Set Up Your MySQL Database
Log into your local MySQL command line interface workbench and build the database using the following execution script:
```sql
CREATE DATABASE student_management;
USE student_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(100),
    year INT
);

CREATE TABLE marks (
    mark_id INT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(100),
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);
```

### 2. Launch the Application
Clone the repository:
```bash
git clone https://github.com/kanupriyakhushi-pixel/student-management-system.git
cd student-management-system
```

Install the dependencies:
```bash
pip install mysql-connector-python python-dotenv
```

Run the system controller script:
```bash
python student_management/student_management.py
```

## 📸 Core Analytic Menu
```text
========================== STUDENT MANAGEMENT SYSTEM ==========================
1. Add Student                 8. Top Performer
2. Search Student               9. Failed Students
3. Remove Student              10. Course-wise Performance
4. Display Students            11. Student-specific Performance
5. Add Marks                   12. Student Ranking
6. Display All Marks           13. Subject-wise Performance
7. Student Performance         14. Exit
```

## 📚 Core Engineering Concepts Mastered
* **Relational Database Design:** Normalising relational database structures to prevent data anomalies.
* **SQL Join Analytics:** Using `INNER JOIN` and `GROUP BY` logic patterns to safely isolate complex multidimensional datasets.
* **Environment Sandboxing:** Hiding core runtime credentials inside system paths to align with modern corporate development operations.

## 🌟 Future Milestones
* Integrate automated **CGPA/GPA conversion matrixes** into menu rankings.
* Convert backend logic components into a desktop graphic wrapper using **CustomTkinter**.
* Deploy data reporting loops to pipe analytic outputs into auto-generated **Excel (.xlsx)** document packages.

## 👩‍💻 Author

**Kanupriya Upadhyay**  
*B.Tech AI & DS Student*  
Learning Python, Data Analytics, SQL, DSA, Machine Learning, and AI Solutions.
