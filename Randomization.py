import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)


# heads = 0
# tails = 1
# coin_flip = random.randint(0, 1)
# if coin_flip == 0:
#     print("Heads")
# else:
#      print("Tails")


# #Lists

# states_in_nigeria = ["Abia", "Adamawa", "Akwa-ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross-river", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu"]

# print(states_in_nigeria[2])
# print(states_in_nigeria[4])

# # Negative indexing starts from behind
# states_in_nigeria.append("Gombe")
# print(states_in_nigeria)

# print(states_in_nigeria[-1])

# states_in_nigeria.append("Jigawa")
# print(states_in_nigeria)

# #To extend a list, we have to use the extend function

# states_in_nigeria.extend(["Kaduna", "Kano", "Kastina", "Kebbi", "Kogi"])

# print(states_in_nigeria)


# # to randomly decide who pays the bills

# bill_payer = ["uche", "chimsom", "pascal", "David", "fafa", "Oge"]

# food = len(bill_payer)
# pay =random.randint(0, food - 1)
# print(bill_payer[pay])



# # Rock Paper Scissors Game



# # Rock
# Rock = ("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)

# # Paper
# Paper = ("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)

# # Scissors
# Scissors = ("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)


# computer_hand = random.randint(1, 3)
# print("Welcome to the game of Rock, Paper and Scissors\n""You are to play first")
# my_hand = input("Choose your hand: ")
# if my_hand == "Rock":
#     print(Rock)
#     if computer_hand == 1:
#         print(Rock)
#     elif computer_hand == 2:
#         print(Paper)
#     elif computer_hand == 3:
#         print(Scissors)
#     if computer_hand == 1 and my_hand == "Rock":
#         print("It's a draw!")
#     elif computer_hand == 2 and my_hand == "Rock":
#         print("You lose!!")
#     elif computer_hand == 3 and my_hand == "Rock":
#         print("You win!")     
# elif my_hand == "Paper":
#     print(Paper)
#     if computer_hand == 1:
#         print(Rock)
#     elif computer_hand == 2:
#         print(Paper)
#     elif computer_hand == 3:
#         print(Scissors)
#     if computer_hand == 1 and my_hand == "Paper":
#         print("You win!!")
#     elif computer_hand == 2 and my_hand == "Paper":
#         print("It's a draw!!")
#     elif computer_hand == 3 and my_hand == "Paper":
#         print("You lose!!")
# elif my_hand == "Scissors":
#     print(Scissors)
#     if computer_hand == 1:
#         print(Rock)
#     elif computer_hand == 2:
#         print(Paper)
#     elif computer_hand == 3:
#         print(Scissors)
#     if computer_hand == 1 and my_hand == "Scissors":
#         print("You lose!!")
#     elif computer_hand == 2 and my_hand == "Scissors":
#         print("You Win!!")
#     elif computer_hand == 3 and my_hand == "Scissors":
#         print("It's a draw!!") 
# else:
#     print("Invalid Option")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(1, nr_letters + 1):
    random_character = random.choice(letters)
    password += random_character
    print(password)
