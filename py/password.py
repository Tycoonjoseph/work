import string

special_chars = "!@#$%^&*"

while True:
    password = input("Enter a password: ")

    errors = []

    # Rule 1: length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Rule 2: number check
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")

    # Rule 3: uppercase check
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Rule 4: special character check
    if not any(char in special_chars for char in password):
        errors.append("Password must contain at least one special character (!@#$%^&*).")

    # Decision
    if not errors:
        print("Strong password accepted ✅")
        break
    else:
        print("\nWeak password ❌")
        for error in errors:
            print("-", error)
        print("\nTry again.\n")