import json
import os
import platform
import pygame

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
   prompt_sample_select()


def load_genres():
    global genres
    try:
        with open('genres.json', 'r') as file:
            data = json.load(file)
            print("Here are the genres you can preview:\n")
            genres = list(data.get("genres"))
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
    global genres, active_genre
    genre_selection = input("What would you like to listen to? (Enter a genre number)")
    
    if genre_selection.isdigit() and int(genre_selection) < len(genres):
        active_genre = genres[int(genre_selection)]
    else:
        print("Please choose a number 0-9")
        prompt_genre_select()

def prompt_sample_select(genre):
    if not genre:
        raise Exception("Genre doesn't exist.")
    for index, sample in enumerate(genre["samples"]):
        print(f"{index} {sample['name']}")

def play_sample(path):
    if not path or not os.path.exists(path): 
        raise Exception("File sample does not exist!")
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    sound.play()

# pygame.init()
# pygame.mixer.init()
# sound = pygame.mixer.Sound("accompany-guitar.wav")
# sound.play

# while pygame.mixer.get_busy():
#     pygame.time.Clock().tick(10)

init()