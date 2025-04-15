import os
import platform


print("Welcome to Sample Player")

def init():
    password_check()

def main_program():
    clear_console()
    print("Access granted. Welcome to Soundboard!")

def password_check():
    password = "Soundboard"
    user_input = input("Enter the password:\n")

    if user_input == password:
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

init()