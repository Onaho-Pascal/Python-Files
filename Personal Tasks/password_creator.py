# Using a while loop, keep asking the user for a password until it:
# is at least 8 characters long, has at least a digit, has at least one uppercase letter




while True:
    password = input("Please input a password:\n")
    if len(password) >= 8:
        has_digit =any(char.isdigit() for char in password)
        has_upper =any(char.isupper() for char in password)
        if has_digit and has_upper:
            print("Thank you")
            break
        else:
            print("password needs at last a digit and one uppercase")
    else:
        print("error")