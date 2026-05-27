# This program prompts the user to enter a number and checks if it is even or odd.
###
while True:
    try:
        number = int(input("Enter a number: "))

        if number % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
            break
    except ValueError:
        print("invalid input. please enter a number.")
###
# this program will check if the number is integer or not
try: 
    x = int(input("What's x? "))
except ValueError:
    print("X is not an integer.")
else:
    print(f"x is {x}.")