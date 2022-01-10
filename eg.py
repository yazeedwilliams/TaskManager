# task 25 task_manager

import datetime 
import re
# Promt user to insert their credentials
f_user = open("user.txt", "r+")
user_txt = f_user.read()

# I created these list to store the values from the text files 
names = []
passwords = []

#This is the array variable that i split first in order to get the names and passwords as one index character
user_txt_array = user_txt.strip().split("\n")

# This for loop will go through the userTxt_array which is the text file names split and then we will split it again but store each variable in the variable name and passwords
#Since each name and password holds one index position, we split them up using the comma and space that way they we can manipulate them easier
for user in user_txt_array:
    loginInfo = user.split(", ")
    names.append(loginInfo[0])      #For every word at the index position of 0 we will add it to the names variable above. This will loop through and keep adding the user names in the array above.
    passwords.append(loginInfo[1])  #This adds all the passwords to the passwords array above 

#Prompt to get user Login name and password
username = input("Enter Your Username: \n")
password = input("Enter Your Password: \n")

#The index function below throws an error if the item is not found in the array, so we manage the error by using the try and except
try:
    index = names.index(username)
except ValueError:
    index = -1

#The while loop using the index function will check to see if the user entered a password or name that match each other at their indexed positions, if not the program will keep prompting them to enter the right details.
while index == -1:
    print("Please Enter a Valid Username & Password")
    username = input("Enter Your Username: \n")
    password = input("Enter Your Password: \n")
    try:
        index = names.index(username)
    except ValueError:
        index = -1
    

def reg_user(new_user):
    

    new_username = input("Please insert a new username: ")
    
    with open('user.txt') as f:
        counter = 0
        while counter < 1:
            if new_username in f.read():
                counter = counter - 1
                print("This username already exists")
                new_username = input("Please insert a new username: ")

            if new_username not in f.read():
                    counter = 2

    new_password = input("Please insert the new user password: ")
    new_password_check = input("Please re-type to confirm your password: ")
    
    while new_password != new_password_check: # while loop to loop until new_password match new_password_check is true
        print("\nThey Do not match, please try again")
        new_username = input("Please insert the new username: \n")
        new_password = input("Please insert the new user password: \n")
        new_password_check = input("Please re-type to confirm your password:\n")

    # if statement to double check that passwords match and then writes it on the txt file
    if new_password == new_password_check:
        print("both passwords match")
        add_new_user = new_username + ", " + new_password
    
    
    f1 = open("user.txt", "a")
    f1.write("\n" + add_new_user)
    f1.close()

def add_task(add_new_task):
    # creating variables for user inputs to be stored
    nw_tsk_usr = input("please insert the username of the person \nyou would like to assgin the task to: ")
    nw_tsk_title = input("Please insert a title for the task: ")
    nw_tsk_des = input("Please insert a description for the task: ")
    nw_due_date = input("Please insert a due date for the task: ")
    tsk_comp = "no"

    # opens and writes those variable to the tasks.txt file
    f2 = open("tasks.txt", "a")
    f2.write("\n"+nw_tsk_usr+", " + nw_tsk_title + ", " + nw_tsk_des + ", " + nw_due_date+ ", "+tsk_comp)
    f2.close()

def view_all(all_tasks):
    f3 = open("tasks.txt", "r")
    tasks_contents = f3.readlines() # Readlines from the text file as an index
        
    # printing each line as a index in a readable format
    print("Task1:")
    print(tasks_contents[0]) 
    print("\nTask 2:")
    print(tasks_contents[1])
    print("\nTask 3:")
    print(tasks_contents[2])

    f3.close()

def view_mine(my_tasks):

    user_task_view = input("Enter username to view your tasks:\n")
    with open("tasks.txt", "r+") as f4:
        
        read_tasks = f4.readlines() # reading lines from the tasks.txt
        print(read_tasks)
        i = 1
        for (user) in read_tasks:
            user_task_info = user.split(",")
            print(user)
            
            if user_task_view == user_task_info[0]:
                print("task",i,":")
                print(user)
                i = i +1
            
        print("Please select")    
        task_selection = int(input("Task number:\n-1 - return to main menu:\n"))      
        if task_selection == -1:
            if username == "admin" and password == "adm1n":
                option = input("\nYou have Admin access\nPlease Select One of The Following Options:\nr - Register User\na - Add Tasks\nva - View All Tasks\nvm - View All My Tasks\ngr - Generate Reports\ns - Statistics\ne - Exit\n")                            # password[1] is in user.txt

    #If the password is correct then the prompt will kick in and show the user our options for them 
            elif password == passwords[index]:
                option = input("\nYou have access\nPlease Select One of The Following Options:\nr - Register User\na - Add Tasks\nva - View All Tasks\nvm - View All My Tasks\ne - Exit\n")                            # password[1] is in user.txt
        
        elif task_selection > 0:
            print("You have selected task:",task_selection,"for user:", user_task_view)
            print(read_tasks[int(task_selection)])

            read_task_edit = read_tasks[1]

            print("1 - Would you like to mark as complete: ")
            print("2 - Edit task: ")
            task_mark_edit = input()

            if task_mark_edit == 1:
                print("You have selected to mark this task")
                yes_no = input("Is this task completed: ")
                if yes_no == 'yes':

                    for line in read_tasks[task_selection]:
                        read_tasks.write(line.replace('no', 'yes'))

                    print("You have marked task:",task_selection,"for user:", user_task_view, " as Complete")
                
                else:
                    print("You chose not to mark the task as complete")
            elif task_mark_edit == 2:
                print("You have selected to edit the task")

                if read_tasks[task_selection] == 'no':
                    print("\nThis task may be edited")
                    edit_tsk_usr = input("please insert the username of the person \nyou would like to assgin the task to: ")
                    edit_due_date = input("Please insert a due date for the task: ")
                    read_tasks.write(line.replace(user_task_info,edit_tsk_usr))

def user_ov(user_reports):
    with open('user.txt','r') as f_usr_report:

        
        lines = f_usr_report.readlines()
        user_split = lines[0].split(',')
        user_split2 = lines[1].split(',')

        user_1 = user_split[0]
        user_2 = user_split2[0]
        
        
        user_task_nums = len(lines)
        user_count = len(loginInfo)
        i = -1

        with open('tasks.txt','r')as f_user_reports2:
           
            user_task_read = f_user_reports2.read()
            user_task_content = f_user_reports2.readlines()
            
            total_No_tasks = len(user_task_content)

            user_tasks_1 = user_task_read.count(user_1)
            user_tasks_2 = user_task_read.count(user_2)
            user_task_com = user_task_read.count ('no') + user_task_read.count('No')
            total_completed_task = user_task_read.count('yes' and 'Yes')

            user_incomp_perc = user_task_com / user_tasks_1 * 100
            user_comp_perc = total_completed_task / user_tasks_1
    with open('user_overview.txt','w') as f_user_ov:
            
        f_user_ov.write("Total number of users: "+str(user_task_nums))
        f_user_ov.write("\nTotal number of tasks: "+str(total_No_tasks))
        f_user_ov.write("\nTotal number of tasks for: "+str(user_1)+" - "+str(user_tasks_1))
        f_user_ov.write("\nTotal percentage of task that have been completed for: "+str(user_1)+" - "+"0")
        f_user_ov.write("\nTotal percentage of task that must still be completed for: " + str(user_1)+ " - " +"100")            
        f_user_ov.write("\nTotal number of tasks for: "+str(user_2)+" - "+str(user_tasks_2))
    
    print("report has been written to the user_overview.txt")

def task_ov(all_reports):
    with open('tasks.txt','r') as f_report:
        
    # Will contain the entire content of the file as a string
        content = f_report.read()
        task_cont = f_report.readlines()

        print(content)
    
        total_number_task = content.count('\n') 
        total_completed_task = content.count('yes' and 'Yes')
        total_no_task = content.count ('no') + content.count('No')
        task_split = content.split(',')

        task_date_1 = task_split[4]
        task_date_2 = task_split[9]
        task_date_3 = task_split[13]
        counter = 0

        if "2019" in task_date_1:
            task1_od = "yes"
            if task1_od == "yes":
                counter = counter + 1
            else:
                counter = counter
        

        if "2019" in task_date_2:
            task2_od = "yes"
            if task2_od == "yes":
                counter = counter + 1
            else:
                counter = counter

        if "2020" in task_date_3 :
            task3_od = "no"  
            if task3_od == "yes":
                counter = counter + 1
            else: counter = counter  
    print("report has been written to the task_overview.txt")
      

    incom_perc = total_no_task / total_number_task * 100
    overdue_perc = counter / total_number_task * 100
    with open('task_overview.txt','w') as f_overv:
        f_overv.write("Total Tasks: " + str(total_number_task))
        f_overv.write("\nTotal Completed Tasks: " + str(total_completed_task))
        f_overv.write("\nTotal Incompleted Tasks: "+ str(total_no_task))
        f_overv.write("\nTotal tasks that are incomplete and overdue:"+str(counter))
        f_overv.write("\nPercentage of incomplete Tasks: "+ str(incom_perc))
        f_overv.write("\nPercentage of task overdue: "+ str(overdue_perc))
    
option = ""    
# This if function will run first to check for a specific username and password
while option != 'e':
    if username == "admin" and password == "adm1n":
        option = input("\nYou have Admin access\nPlease Select One of The Following Options:\nr - Register User\na - Add Tasks\nva - View All Tasks\nvm - View All My Tasks\ngr - Generate Reports\ns - Statistics\ne - Exit\n")                            # password[1] is in user.txt

    #If the password is correct then the prompt will kick in and show the user our options for them 
    elif password == passwords[index]:
        option = input("\nYou have access\nPlease Select One of The Following Options:\nr - Register User\na - Add Tasks\nva - View All Tasks\nvm - View All My Tasks\ne - Exit\n")                            # password[1] is in user.txt
                

    # r selection from the list
    if option == "r":
        
        if username == "admin" and password == "adm1n":   

            print("You have admin rights")
            print("\nYou have selected to register a new user:")
            reg_user(1)
            
        else: print("You do not have admin rights")


    elif option == "s":
        if username == "admin" and password == "adm1n":

            print("You have chosen statstics:")

            f3 = open("tasks.txt", "r")
            contents = f3.readlines() # Readlines from the text file as an index
            count_tasks = len(contents)
            print("amount of tasks:")
            print(count_tasks)
            f3.close()
        
            f5 = open("user.txt", "r")
            users_data = f5.readlines()
            count_users = len(users_data)
            print("\nAmount of users:")
            print(count_users)

            print("\nTask overview:")
            with open('task_overview.txt','r') as f_stats_ov:
                task_overview = f_stats_ov.readlines()
                print(task_overview)
            
            print("\nUser Overview:")
            with open('user_overview.txt','r') as f_user_ov:
                user_overview  = f_user_ov.readlines()
                print(user_overview)

        else: 
            print("You do not have admin rights")
        


    # a option from the selection list
    elif option == "a":
        print("\nYou have selected to add a new task")
        
        print(add_task(1))

    # va option from selection
    elif option == "va":
        print("\nYou have selected to view all tasks")
        print(view_all(1))

    # vm option from selection
    elif option == "vm":
        print("\nYou have selected View My Tasks: ")

        print(view_mine(1))    

    elif option == "gr":
        print("You have selected to Generate Reports: ")
        print(task_ov(1))
        print(user_ov(1))

    elif option == "e":
        print("You have chosen to Exit the program")
        exit(0)
    else:
        print("you have selected an invalid option")

f_user.close()
