import random
Games = ["Mk1", "SF6", "Tekken"]
for Game in Games:
    print(Game)
total_height = 0
students_height = [30, 27, 28, 22, 24, 29, 23]
for height in students_height:
    total_height += height
print(total_height)

# Adding numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)

# Adding even numbers from 1 to 100

even_numbers = 0
for even in range(2, 102, 2):
    even_numbers += even
print(even_numbers)

for num in range(1, 101):
    print(num)
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")

    
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy level
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for symb in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)

# # # Hard level
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for symb in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(password)


import random
score = ["10", "73", "41", "99", "89"]
print(score)

random.shuffle(score)
password = "".join(score)
print(password)