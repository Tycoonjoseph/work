"""This program demonstrates the use of command line arguments in Python. It takes a name as an argument and prints a greeting. It also handles exceptions for missing or too many arguments.
# use of the command line arguments inspired by cs50's lecture on command line arguments
import sys
# solve an exception using the try and except if the user does not provide a name
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Usage: python script.py <name>")
# to solve an exception using the if statement
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
#to solve an exception using the if statement and exit the program
if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit(1)
else:
    print("Hello, my name is", sys.argv[1])"""
# to iterate through the command line arguments using a for loop
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")   
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)