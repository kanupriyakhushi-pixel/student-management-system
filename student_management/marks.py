
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kanu@1707",
    database="student_management"
)
cursor = connection.cursor()

while True:
    try:
        print("==========================MARKS MANAGEMENT SYSTEM==========================")
        print("1. Add mark_id\n2. Display all marks\n3. Student Performance\n4.Dispaly top performer \n5. Display failed students\n6.Course Wise Perofrmance\n7. Student Specific Performance\n8. Student Ranking\n9. Subject Wise Performance\n10. Exit")
        enter_choice= int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    if enter_choice==1:
        add_marks_id=int(input("Add marks_id: "))
        add_student_id=int(input("Add student_id: "))
        add_marks=int(input("Add marks: "))
        add_subjects=input("Add subjects: ")
        cursor.execute("insert into marks(mark_id,student_id,subject,marks) values(%s,%s,%s,%s)", (add_marks_id, add_student_id, add_subjects, add_marks))
        connection.commit()
    elif enter_choice==2:
        cursor.execute("select * from marks")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==3:
        cursor.execute("select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students inner join marks on marks.student_id=students.student_id group by name;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==4:
        print("==========================TOP PERFORMER==========================")
        cursor.execute("select name as student, avg(marks) as average_marks from students inner join marks on marks.student_id=students.student_id group by name order by avg(marks) desc limit 1;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==5:
        print("==========================FAILED STUDENTS==========================")
        cursor.execute("select name as student, subject ,marks from students inner join marks on marks.student_id=students.student_id where marks <40;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==6:
        print("==========================COURSE WISE PERFORMANCE==========================")
        cursor.execute("select course, avg(marks) as average_marks from students inner join marks on marks.student_id=students.student_id group by course;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==7:
        print("==========================STUDENTS SPECIFIC PERFORMANCE==========================")
        student_id=input("enter student id to search :")
        cursor.execute("select subject ,marks from students inner join marks on marks.student_id=students.student_id where student_id=%s;", (student_id,))
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==8:
        print("==========================STUDENTS RANKING==========================")
        cursor.execute("select name as student, sum(marks) as total_marks , avg(marks) as Average_marks from students inner join marks on marks.student_id=students.student_id group by name order by avg(marks) desc;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==9:
        print("==========================SUBJECT WISE PERFORMANCE==========================")
        cursor.execute("select subject, avg(marks) as average_marks from marks group by subject;")
        results=cursor.fetchall()
        for i in results:
            print(i)
    elif enter_choice==10:
        connection.close()   
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 10.")