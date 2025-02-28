# I want to create an algorithm that would grant provide password to a user only if the user is authorized.
# The user, however, can only be authorized if they are equal to or above 18 years of age.

# Step 1: Password Generator

import random

letters = ["a", "c", "b", "x", "m", "p", "l", "h", "j","k", "i", "r", "G", "Q", "q", "T", "W"]
numbers = ["1", "5", "3", "9", "4", "2", "6", "7", "8", "0"]
symbols = ["*", ")", "#", "%", "!"]

password = []
for letter in range(0, 6):
    password += random.choice(letters)
for number in range(0, 3):
    password += random.choice(numbers)
for symbol in range(0, 3):
    password += random.choice(symbols)

random.shuffle(password)
password = "".join(password)



#Step 2: Create the prompt for the information to access generated password.

try:
    print("Welcome to this exercise")
    name = str(input("Input your name: \n"))
    age = int(input("How old are you?: \n"))
    if age >= 18:
        print(f"Welcome, {name}!\nNow, let us give you a password :)")
        print(f"Your password is\n{password}")
    else:
        print("You are not authorized")
except ValueError:
    print("Invalid Input. Please Enter a number.")