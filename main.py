import json
import os
import platform

username = "User"
genres = []
active_genre = None

def init():
    print("Welcome to Sample Player")
    password_check()

def main_program():
   user_name()
   load_genres()
   prompt_genre_select()

def load_genres():
    try:
        with open('genres.json', 'r') as file:
            data = json.load(file)
            print("Here are the genres you can preview:\n")
            genres = data.get("genres")
            for i, genre in enumerate(genres):
                print(i, genre)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid Json.")

def password_check():
    password = "Soundboard"
    user_input = input("Enter the password:\n")

    if user_input == password:
        clear_console()
        print("Access granted. Welcome to Soundboard!\nIn this program you can choose a genre and play sounds related to that genre.")

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

def prompt_genre_select():
    genre_selection = input("What would you like to listen to? (Enter a genre number)")
    print('genre_selection.isdigit()', genre_selection.isdigit())
    print('int(genre_selection)', int(genre_selection))
    print('len(genres)', len(genres))
    if genre_selection.isdigit() and not int(genre_selection) > len(genres):
        active_genre = genres[int(genre_selection)]
    else:
        print("Please choose a number 0-9")
        prompt_genre_select()

init()