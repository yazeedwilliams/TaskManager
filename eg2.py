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
S - Statistics
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
def view_more():
        username = input("Please enter the username which you want to view the tasks for?\n")
        num_task = 0     
        view_more = open('tasks.txt', 'r')
        for row in view_more:
                field = row.strip().split(",")
                num_task += 1
                if username == field[0]:
                        print("Task Number: " + str(num_task) + "\nUsername: " + field[0] + "\nTitle: " + field[1] + "\nDescription: " + field[2] + "\nDue Date: " + field[3] + "\nCompleted: " + field[4] + "\n")

        editTask = input("Would you like to edit a task? (Edit) or return to the menu? (-1)\n")
        if editTask == "Edit":
            taskNum = int(input("Please enter the Task number?\n"))
            taskNum = taskNum - 1
            file = open('tasks.txt', 'r')
            taskFile = file.readlines()
            for line in taskFile:
                print(taskFile[taskNum] + "\n")
                break

            taskComplete = input("Has this task been completed?\n")
            if taskComplete == "Yes":
                userTask = taskFile[taskNum].strip().split(",")
                userTask[4] = "Yes"
                print(userTask)

            elif taskComplete == "No":
                userTask = taskFile[taskNum].strip().split(",")
                userTask[4] = "No"
                file.write(userTask[4])

        elif editTask == "-1":
            displayMenu()

view_more()
        

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

elif option == "a":
    add_task()

elif option == "va":
    view_all()

elif option == "vm":
    view_more()

elif option == "e":
    exit()

else:
    invalid_option()
