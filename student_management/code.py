f=open('student_management/students.txt','r')
text= f.read()
student_list=text.splitlines()
print(student_list)
f.close()

def save_students():
    f=open('student_management/students.txt','w')
    for student in student_list:
        f.write(student + '\n')
        
    f.close()
def search_student(student_name):
    
    if student_name in student_list:
        print("student found!")
    
    else:
        print("student not found in list")

def remove_student(student_name):
    if student_name in student_list:
        student_list.remove(student_name)
        save_students()
        print("student removed successfully")
    else:
        print("student not found in list")
    
        
    
    
    
                

while True:
    try:
        print("1. Add student\n2. Search student\n3. Remove student\n4. Display student list\n5. Exit")
        enter_choice= int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    else:
        print("Invalid choice!")

    if enter_choice==1:
        add_name= input("Add student name : ")
        student_list.append(add_name)
        save_students()
        
        

    elif enter_choice==2:
        search_student(student_name=input("enter student name to search :"))
        
    elif enter_choice==3:
        student_remove=input("enter student name to remove :")
        remove_student(student_name=student_remove)
    elif enter_choice==4:
        print(student_list)
        
    elif enter_choice==5:

        print("Exiting...")
        break
    else:
        print("invalid choice")
    
    
                    
                
            
    


                        
            
    
    
            
    



    




