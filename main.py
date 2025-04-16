import os
import platform

username = "User"

def init():
    print("Welcome to Sample Player")
    password_check()

def main_program():
   user_name()
   

def password_check():
    password = "Soundboard"
    user_input = input("Enter the password:\n")

    if user_input == password:
        clear_console()
        print("Access granted. Welcome to Soundboard!")
        main_program()
    else:
        print("Access denied. Incorrect password.") 
        response = input("Try again? (Y/N)")
        if response == "y" or response == "Y":
            clear_console()
            init()
        else:
            end_program()    

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def end_program():
    clear_console()
    print("Exiting program")

def user_name():
    username = input("What is your Name?\n")
    if username.isalnum() and not username.isdigit() and not len(username) > 20:
        print(username + "'s Soundboard")
    else:
        print("Please enter a valid username, ex. Jimbob15 (less than 20 characters)")
        user_name()



init()