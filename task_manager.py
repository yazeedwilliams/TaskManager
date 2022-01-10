# program that manages tasks assigned to members of a team of a small business

# login
# the user will be prompted to enter the details
# if it corresponds to the data in the user.txt file it will allow them to log in
login = False

while login == False:
    user_file = open("user.txt", "r+")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for line in user_file:
        valid_username, valid_password = line.split(", ")

        if valid_username == username and valid_password == password:
            login = True

    if login == False:
        print("Username or password is invalid!")

    user_file.seek(0)

# if the user is the admin then it will display an extra option (s - statistics)
# if the user is not admin it will display the normal options

if username == "admin":
    option = input("""
Please select one of the following options:
r - Register a user
a - Add a task
va - View all tasks
vm - View all my tasks
s - Statistics
gr - Generate reports
e - Exit
""")

else:
    option = input("""
Please select one of the following options:
r - Register a user
a - Add a task
va - View all tasks
vm - View all my tasks
e - Exit
""")

# this section takes the input of the user and displays the appropriate inputs    
# registering a user
def reg_user():
    user_file = open("user.txt", "a+")
    new_username = input("Enter a username: ")
    
# while statement to check if the username already exists
    while new_username == valid_username:
        print("Username already exists")
        new_username = input("Enter a username: ")
        
    new_password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")

# while statement is used to check if the passwords match. If it does not match it loops through the process again until there is a match
    while confirm_password != new_password:
        print("Passwords do not match! Please try again")
        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        confirm_password = input("Confirm password: ")

    if confirm_password == new_password:
        user_file.write(f"\n{new_username}, {new_password}")

        print("You have successfully registered a new user")

    user_file.seek(0)            # .seek() moves the cursor to the beginning of the text file
    user_file.close()

# displaying the statistics (only for admin)
# used https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/ as a reference
def stats():
    if username == "admin":
        user_file = open("user.txt", "r")
        count_users = 0
        content1 = user_file.read()
        user_list = content1.split("\n")      # splits the list wherever there is an "\n". 

        for count1 in user_list:
            if count1:
                count_users += 1

        tasks_file = open("tasks.txt", "r")
        count_tasks = 0
        content2 = tasks_file.read()
        tasks_list = content2.split("\n")

        for count2 in tasks_list:
            if count2:
                count_tasks += 1
                
        print(f"The number of users: {count_users}")
        print(f"The number of tasks: {count_tasks}")

# if the user is not admin then an error message will be displayed
    else:
        print("You are not admin")
    
# adding a task
def add_task():
    tasks_file = open("tasks.txt", "a+")

    user = input("Enter the username that this task will be assigned to: ")
    task_name = input("Enter the name of the task: ")
    task_description = input("Enter the description of the task: ")
    start_date = input("Enter the date that this task was assigned (dd/mm/yyyy): ")
    due_date = input("Enter the date that this task must be done by (dd/mm/yyyy): ")
    completed = "No"

    tasks_file.write(f"\n{user}, {task_name}, {task_description}, {start_date}, {due_date}, {completed}")
    user_file.seek(0)
    tasks_file.close()

# viewing all tasks
def view_all():
    tasks_file = open("tasks.txt", "r")

    for line in tasks_file:
        user, task_name, task_description, start_date, due_date, completed = line.split(", ")
        print(f"""
Task:             {task_name}
Assigned to:      {user}
Task description: {task_description}
Date assigned:    {start_date}
Due date:         {due_date}
Task completed?:  {completed}
""")

    tasks_file.close()

# viewing my tasks
def view_mine():
    tasks_file = open("tasks.txt", "r")
    task_num = 0

    for line in tasks_file:
        user, task_name, task_description, start_date, due_date, completed = line.split(", ")
        task_num += 1
        
        if username == user:          # this checks that the user currently logged in will be displayed their tasks only
            print(f""" 
Task:             {task_name}
Task number:      {task_num}
Assigned to:      {user}
Task description: {task_description}
Date assigned:    {start_date}
Due date:         {due_date}
Task completed?:  {completed}
""")

    tasks_file.close() 

    task_menu = int(input("Enter task number to select a specific task or enter -1 to return to the main menu: \n"))
    if task_menu >= 1:
        task_menu -= 1
        my_task_file = open("tasks.txt", "r")
        my_tasks = my_task_file.readlines()
        for number in my_tasks:
            print(my_tasks[task_menu] + "\n")
            break                              # the break keyword allows only the task entered to be displayed

        my_task_file.close()

        tasks_file = open("tasks.txt", "a+")
        for line in tasks_file:
            user, task_name, task_description, start_date, due_date, completed = line.split(", ")
        
        complete_edit = input("Enter (complete) to mark task as complete or enter (edit) to edit the user assigned or edit the due date: \n").lower()
        if complete_edit == "complete":
            task_complete = input("Is this task completed (Yes or No)").lower()
            if task_complete == "yes":
                completed = "Yes"
                tasks_file.write(f"\n{user}, {task_name}, {task_description}, {start_date}, {due_date}, {completed}")

            elif task_complete == "No":
                completed = "No"
                tasks_file.write(f"\n{user}, {task_name}, {task_description}, {start_date}, {due_date}, {completed}")

#    elif task_menu == -1:
#        main_menu()

def reports():
# coutning the number of tasks in the file
    tasks_file = open("tasks.txt", "r")
    count_tasks = 0
    content1 = tasks_file.read()
    tasks_list1 = content1.split("\n")

    for count1 in tasks_list1:
        if count1:
            count_tasks += 1
                
    print(f"The number of tasks: {count_tasks}")
    tasks_file.close()

# counting the number of completed tasks
    tasks_file = open("tasks.txt", "r")
    completed_list = []
    for count2 in tasks_file:
        user, task_name, task_description, start_date, due_date, completed = line.split(", ")
        completed_list.append(completed)
    completed_list2 = []
    for element1 in completed_list:
        ompleted_list2.append(element1.strip())

    completed_count = completed_list.count("Yes")
    print(f"The number of incompleted tasks: {completed_count}")
    tasks_file.close()

# counting the number of incompleted tasks
    tasks_file = open("tasks.txt", "r")
    incompleted_list = []
    for count3 in tasks_file:
        user, task_name, task_description, start_date, due_date, completed = line.split(", ")
        incompleted_list.append(completed)
        incompleted_list2 = []
        for element2 in incompleted_list:
            incompleted_list2.append(element2.strip())

    incompleted_count = incompleted_list2.count("No")
    print(f"The number of incompleted tasks: {incompleted_count}")
    tasks_file.close()
        
       
def exit():
    print("Thank you for using TaskManager")
    exit(0)

# if the user enters anything else other than what the menu displays, an error message will be displayed
def invalid_option():
    print("You have selected an invalid option! Please restart the program.")
    

# calling functions
if option == "r":
    reg_user()

elif option == "s":
    stats()

elif option == "gr":
    reports()

elif option == "a":
    add_task()

elif option == "va":
    view_all()

elif option == "vm":
    view_mine()

elif option == "e":
    exit()

else:
    invalid_option()
