
student_list=[]
while True:
    print("1. Add student\n2. Search student\n3. Remove student\n4. Display student list\n5. Exit")
    enter_choice= int(input("Enter your choice: "))
    
    if enter_choice==1:
        
        for i in range(1,6):
            add_name= input("Add student name : ")
            student_list.append(add_name)

    elif enter_choice==2:
        student_search=input("enter student name to search :")
        if student_search in student_list:
            print("student found!")

        else:
            print("student not found in list")
        
    elif enter_choice==3:
        student_remove=input("enter student name to remove :")
        if student_remove in student_list:
            student_list.remove(student_remove)
            print("student removed successfully")
        else:
            print("student not found in list")
    elif enter_choice==4:
        print(student_list)
        
    elif enter_choice==5:

        print("Exiting...")
        break
    else:
        print("invalid choice")
    
    
                    
                
            
    


                        
            
    
    
            
    



    




