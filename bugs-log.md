# Bugs log

This is where i will track my bugs and add their resolutions. 

## Bug 1: Couldn't run the main.py file from the command line

I was creating a Hello world print line statement, but got a syntax error:

```bash
python3 
Python 3.9.6 (default, Feb  3 2024, 15:58:27) 
[Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> python3 main.py
  File "<stdin>", line 1
    python3 main.py
            ^
SyntaxError: invalid syntax
>>> q
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'q' is not defined
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> ^D
leo@pauls-mac-mini sample-player % python3 main.py
Welcom to Sample Player
leo@pauls-mac-mini sample-player % 
```

I accidentally pressed enter after typing python before I could write my next argument. Due to this all command following that action was executed in the repl.

## Bug 2: error using `pyinstaller`

 I'm trying to package my code into an executable. Trying to use `pyinstaller` a common package for this. `pip install` succeeds but I get this error when i try to run it:

```bash
leo@pauls-mac-mini sample-player % pyinstaller --onefile m
ain.py
zsh: command not found: pyinstaller
```

1. I ran activate again: `source venv/bin/activate`
2. Then I reinstalled with `pip pyinstaller`
3. I checked the version using `pyinstaller --version` and it dispayed 6.12.0 at this point it looks like its installed. 
4. Then we ran the packaging command again

That created a /dist folder with the executable in it. I run the executable and the print line opens
 
 ## Bug 3: error trying to exit passowrd flow
 
  I was attempting to create a exiting feature from the password screen.
  When used user is prompted to, yes continue or no exit after a incorrect password input.
  However, when option no was selected user was brought back to the password screen, regardless.

  Source of problem: My if statement was wrong.

  ```python
  if response == "y" or "Y":
  ```
  
  the first half of the if statement will be true if the response is "y" , but if its false it will read `or "Y"` as always true, because it is a non empty stirng
  I should have had this:

  ```python
  if response == "y" or response == "Y":
```




## Bug 4: error attempting to create a username feature

```bash
Access granted. Welcome to Soundboard!
What is your Name?
78834983489389398489498988989
Please enter a valid username, ex. Jimbob15 (less than 20 characters)
What is your Name?
Jimmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy
Traceback (most recent call last):
  File "/Users/leo/Dev/sample-player/main.py", line 48, in <module>
    init()
  File "/Users/leo/Dev/sample-player/main.py", line 8, in init
    password_check()
  File "/Users/leo/Dev/sample-player/main.py", line 20, in password_check
    main_program()
  File "/Users/leo/Dev/sample-player/main.py", line 11, in main_program
    user_name()
  File "/Users/leo/Dev/sample-player/main.py", line 46, in user_name
    user_name()
  File "/Users/leo/Dev/sample-player/main.py", line 42, in user_name
    if username.isalnum() and not username.isdigit() and not username.length < 20:
AttributeError: 'str' object has no attribute 'length'
```

I was checking username.length but turns out `username.length` is for java not python. Instead I should have used the `len()` function.

## Bug 5: error while opening json file

``` bash
/Library/Developer/CommandLineTools/usr/bin/python3: can't open file '/Users/leo/Dev/sample-player/sounds/main.py': [Errno 2] No such file or directory
leo@pauls-mac-mini sounds % python3 main.py
/Library/Developer/CommandLineTools/usr/bin/python3: can't open file '/Users/leo/Dev/sample-player/sounds/main.py': [Errno 2] No such file or directory
```

I was trying to open json file containing sound data, and received the error above. Turns out I was in the "sounds" directory not the "main" directory.


## Bug 6: error while summoning genres file

I was recivein an error that syas it couldn't find the genres property on my python dictionary loaded from json object. accessed the property with a `data.get` instead

## Bug 7: index out of range error selecting a genre

When I tried to set the active genre based on the number of the genre, I get this error if I choose a number greater than the number of genres in the list.

```bash
Traceback (most recent call last):
  File "/Users/leo/Dev/sample-player/main.py", line 75, in <module>
    init()
  File "/Users/leo/Dev/sample-player/main.py", line 11, in init
    password_check()
  File "/Users/leo/Dev/sample-player/main.py", line 39, in password_check
    main_program()
  File "/Users/leo/Dev/sample-player/main.py", line 16, in main_program
    prompt_genre_select()
  File "/Users/leo/Dev/sample-player/main.py", line 70, in prompt_genre_select
    active_genre = genres[int(genre_selection)]
IndexError: list index out of range
```

I fixed this by comparing against the list length instead of a number so we never go out of range.


## Bug 8:pygame import confused interpreter

Defaulting to user installation because normal site-packages is not writeable
Collecting pygame
  Downloading pygame-2.6.1-cp39-cp39-macosx_11_0_arm64.whl.metadata (12 kB)
Downloading pygame-2.6.1-cp39-cp39-macosx_11_0_arm64.whl (12.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 5.3 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.6.1

I fixed this problem by switiching interpreter views to hopefully reload and give the interpreter a chance to understand the code