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