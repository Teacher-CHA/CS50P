"""
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, 
and outputs the number of lines of code in that file, excluding comments and blank lines. 
If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, 
or if the specified file does not exist, 
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) 
Assume that any line that only contains whitespace is blank.
"""
import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count = 0
try:
    with open(sys.argv[1],"r",encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip comment or blank line
            else:
                count += 1
        print(count)

except FileNotFoundError:
    sys.exit("File does not exist.")