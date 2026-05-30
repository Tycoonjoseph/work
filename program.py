#creating a program that can help me solve my daily problems.
def main():
    height = int(input("Height: "))
    while height < 1 or height > 8:
        height = int(input("Height: "))
    for i in range(1, height + 1):
        print("#" * i)
def problem_solver():
    print("This program can help me solve my daily problems.")
    laptop_setup = input("Do you want to set up your laptop? (yes/no) ")
    if laptop_setup.lower() == "yes":
        access = input("Accept to give access to your laptop? (yes/no) ")
        if access.lower() == "yes":
            print("Access granted. setting up your laptop...")
        else:
            print("Access denied. Cannot set up you laptop.")
    else:
        print("Okay, maybe later at you free time.")
def action():
    pass


if __name__ == "__main__":
    action()
    main()
    problem_solver()