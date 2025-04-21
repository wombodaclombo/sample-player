# file name: main.py
#author: Leo Sanders
# date: 4/21/2025
#Description: This project aims  to become a functioning audio player which plays music samples from certain genres when selected. 
# The program loads data from a Json file and then ships it to the program to be processed.

import json
import os
import platform
import pygame
from genre import Genre

username = "User"
genres = []
active_genre = None


def init():
    '''
    Welcomes the user and initiates the password check.
    
    parameters: none
    
    returns none:
    '''
    print("Welcome to Sample Player!")
    password_check()

def main_program():
   '''
   Calls other functions to control the flow of the total program.
   
   parameters none

   returns none
   '''
   global active_genre
   user_name()
   load_genres()
   prompt_genre_select()
   print("Thank you for using SamplePlayer \n Goodbye")


def load_genres():
    '''loads genre information from jsn file which contains genre data
    
    returns none

    parameters none
    
    '''
    global genres
    try:
        with open('genres.json', 'r') as file:
            data = json.load(file)
            for genre in data.get("genres", []):
                genres.append(Genre(genre["name"], genre["samples"]))
            
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid Json.")

def password_check():
    '''Asks user for password, if user enters incorrect password user is 
    prompted to try again, is correct password in entred user is granted access to SamplePlayer'''
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
    '''prompts user for username'''
    username = input("What is your Name?\n")
    clear_console()
    if username.isalnum() and not username.isdigit() and not len(username) > 20:
        print("|***** " +username + "'s Soundboard *****|\n")
    else:
        print("Please enter a valid username, ex. Jimbob15 (less than 20 characters)")
        user_name()

def prompt_genre_select():
    '''Asks user to select genre and draws data from genres.json.'''
    global genres, active_genre
    while True:
        print("Here are the genres you can preview:\n")
        for i, genre in enumerate(genres):
            print(f"{i}: {genre.name}")
        genre_selection = input("What would you like to listen to? (Enter a genre number or 'exit' to exit): ")
        if genre_selection == "exit":
            break
        if genre_selection.isdigit() and int(genre_selection) < len(genres):
            active_genre = genres[int(genre_selection)]
        else:
            print("Invalid selection. Try again.")
        prompt_sample_select(active_genre)

def prompt_sample_select(genre):
    '''Prompts the user to select a sample for the specified genre.
    The user continues to be prompted to select samples to play until they type exit.'''
    if not genre:
        raise Exception("Genre doesn't exist.")
    while True:
        print("Please select a sample number:\n")
        for index, sample in enumerate(genre.samples):
            print(f"{index} {sample['name']}")
        selection = input("\nYour selection (or type exit to quit): ")
        if selection == "exit":
            print("\nExiting...")
            break
        if not selection.isdigit():
            raise Exception("No sample here!\n")
        index = int(selection)
        samples = genre.samples
        path = samples[index].get("file")
        play_sample(path)

def play_sample(path):
    '''Plays the sample at the specified path if it exists. Playback cannot be interrupted.'''
    if not path or not os.path.exists(path): 
        raise Exception("File sample does not exist!")
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    sound.play()
    print("\nPlaying sample...\n")
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)

init()

