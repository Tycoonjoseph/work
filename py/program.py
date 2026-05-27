import random 
import datetime
from xmlrpc.client import boolean
name = str(input("What is your name? ")).capitalize().strip()
is_student = boolean(input("Are you a student? (True/False) "))
age = int(input("What is you age? "))
current_year = datetime.datetime.now().year
birth_year = current_year - age
print(f"Hello {name}, you were born in {birth_year}.")
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
    