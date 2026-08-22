import mysql.connector
import os
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = connection.cursor()
              

while True:
    try:
        print("==========================STUDENT MANAGEMENT SYSTEM==========================")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Display Students")
        print("5. Add Marks")
        print("6. Display All Marks")
        print("7. Student Performance")
        print("8. Top Performer")
        print("9. Failed Students")
        print("10. Course-wise Performance")
        print("11. Student-specific Performance")
        print("12. Student Ranking")
        print("13. Subject-wise Performance")
        print("14. Exit")
        enter_choice= int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    

    if enter_choice==1:
        try:
            add_name= input("Add student name : ")
            add_student_id= int(input("Add student ID : "))
            add_course= input("Add course : ")
            add_year= int(input("Add year : "))
        except ValueError:
            print("Invalid input! Please enter a valid input.")
            continue
        
        cursor.execute("insert into students(name,student_id,course,year) values(%s, %s, %s, %s)", (add_name, add_student_id, add_course, add_year))
        connection.commit()
        

    elif enter_choice==2:
        #search_student(student_name=input("enter student name to search :"))
        student_name=input("enter student name to search :")
        cursor.execute("select * from students where name=%s", (student_name,))
        result = cursor.fetchall()
        for i in result:
            print(i)
    elif enter_choice==3:
        try:
            student_remove= int(input("enter student id to remove :"))
            cursor.execute("delete from students where student_id=%s", (student_remove,))
            connection.commit()
        except ValueError:
            print("Invalid input! Please enter a valid student ID.")
            continue

        
        
    elif enter_choice==4:
        #print(student_list)
        cursor.execute("select * from students")
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif enter_choice==5:

        try:
            add_marks_id=int(input("Add marks_id: "))
            add_student_id=int(input("Add student_id: "))
            add_marks=int(input("Add marks: "))
            add_subjects=input("Add subjects: ")
            cursor.execute("insert into marks(mark_id,student_id,subject,marks) values(%s,%s,%s,%s)", (add_marks_id, add_student_id, add_subjects, add_marks))
            connection.commit()
        except ValueError:
            print("Invalid input! Please enter valid inputs.")
            continue
    elif enter_choice==6:
        cursor.execute("select * from marks")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==7:
        print("==========================STUDENT PERFORMANCE==========================")
        cursor.execute("select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students inner join marks on marks.student_id=students.student_id group by name;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==8:
        print("==========================TOP PERFORMER==========================")
        cursor.execute("select name as student, avg(marks) as average_marks from students inner join marks on marks.student_id=students.student_id group by name order by avg(marks) desc limit 1;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==9:
        print("==========================FAILED STUDENTS==========================")
        cursor.execute("select name as student, subject ,marks from students inner join marks on marks.student_id=students.student_id where marks <40;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==10:
        print("==========================COURSE WISE PERFORMANCE==========================")
        cursor.execute("select course, avg(marks) as average_marks from students inner join marks on marks.student_id=students.student_id group by course;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==11:
        print("==========================STUDENTS SPECIFIC PERFORMANCE==========================")
        try:
            student_id=int(input("enter student id to search :"))
            cursor.execute("SELECT subject, marks FROM marks WHERE student_id=%s",(student_id,))
            results=cursor.fetchall()
            for i in results:
                print(i)
        except ValueError:
            print("Invalid input! Please enter a valid student ID.")
    elif enter_choice==12:
        print("==========================STUDENTS RANKING==========================")
        cursor.execute("select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students inner join marks on marks.student_id=students.student_id group by name order by avg(marks) desc;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==13:
        print("==========================SUBJECT WISE PERFORMANCE==========================")
        cursor.execute("select subject, avg(marks) as average_marks from marks group by subject;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==14:
        connection.close() 
        cursor.close()  
        break
        
    else:

        print("Invalid choice! Please enter a number between 1 and 14.")
        

   
    
    
                    
                
            
    


                        
            
    
    
            
    



    




