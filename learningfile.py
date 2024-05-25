# # # # # testing out print functions
# # # # print("Hello World!")
# # # # print("I am Pascal")

# # # # num1 = input("What was your math score?: ")
# # # # num2 = input("What was your chemistry score?: ")
# # # # print(num1 + num2)

# # # # # using quotes insside a print quote requires alternating the quotes between single and double quotes.
# # # # print('She said: "Hello" and then left.')
# # # # # # Another way would be to place the escape back slash in front of the two interior double quotes
# # # # # # as a way to tell the computer to ignore it as a code and just print it the way you intend. for example:

# # # # print("She said: \"Hello\" and then left.")
# # # # # # now, to test them:
# # # # # # A 'single quote' inside a double quote
# # # # # A "double quote" inside a single quote
# # # # #Alternatively, you can just \"escape\" the quote"

# # # # print("A 'single quote' inside a double quote")
# # # # print('A "double quote" inside a single quote')
# # # # print("Alternatively, you can just \"escape\" the quote")

# # # # # # How to create a new line using the backslash-n \n

# # # # print("Hello world!\nHello world!\nHello world!")

# # # # # # combining two strings
# # # # print("Hello" + " Pascal")
# # # # print("Hello" + " " + "Pascal")

# # # # # Python input function
# # # # # for the input function, the string in the parenthesis is called a prompt. 
# # # # name = input("What is your name?: ")
# # # # print("Hello", name)
# # # # # Another way I can achieve this is by nesting the input function with hello:
# # # # print("Hello " + input("What is your name?: "))
# # # # # For the above line, python first executes the input function then passes the answer into the print function altogether.


# # # # # using the if and is.digit function to filter out strings from values in the prompt
# # # # age = input("How old are you?: ")

# # # # if age.isdigit():
# # # #     if age >= "30":
# # # #         print("Wow, you are", age + "?", "that's quite old, ngl")
# # # #     elif age < "30":
# # # #         print("You are young, that is nice!")
# # # # else:
# # # #     print("That was not what I asked you for dork!")

# # # # # the len function can be used to get the number of characters in a string or the number of strings in a collection
# # # # print(len("Hello"))
# # # # surname = "Onaho"
# # # # print(len(surname))

# # # # name = input("What is your name?: ")
# # # # length = len(name)
# # # # print(length)

# # # # # Band Name Generator
# # # # print("Welcome to the Band Name Generator.")
# # # # city_name = input("what is the name of the city's you grew up in?: \n")
# # # # pet_name = input("What is the name of your pet?: \n")
# # # # print("Your band name could be", city_name, pet_name)



# # # ## Data Types

# # # # to get an index in a string, we put the index position in a square bracket after the string

# # # # print("Hello"[0])
# # # # print("Hello"[4])


# # # # # Large Integers can be written with delimiters as underscores. That is, commas can be written as underscores
# # # # # for example, 123,456,789 can be typed as 123_45_789 and Python will still recognize it as a valid integer.

# # # # print(123_456_789)

# # # # # FLoats are numbers with decimals.

# # # # #Booleans
# # # # True
# # # # False

# # # # # the "type" function checks the type of data in the parenthesis.

# # # # name = "Pascal"
# # # # age = 35

# # # # print(type(name))
# # # # print(type(age))

# # # # name_length = len(name)
# # # # print(type(name_length))


# # # surname = input("What is your surname?: \n")
# # # surname_length = len(surname)

# # # # new_surname_length = str(surname_length)

# # # print("Your surname has", surname_length, "characters")



# # # two_digit_number = input()
# # # print(type(two_digit_number))

# # # double asterisks stand for raise to power or exponential. 2 ** 2 is 2 raised to the power of 2
 
# # # Mathematical equations also follow the PEMDAS or BODMAS rule: Parenthesis, Exponents, Multiplication, Division, Addition, and Subtraction.

# # score = 0
# # #User scores a point

# # score += 1
# # print(score)

# # score = 0
# # height = 1.8
# # isWInning = True
# # #f-string
# # print(f"your score is {score}, your height is {height}, you are winning is {isWInning}")



# print("Welcome to the tip calculator!")

# bill = input("What was the total bill?: ")
# if bill.isdigit():
#     tip = input("How much would you like to give? 10, 12, or 15?: ")
#     if tip in ["10", "12", "15"]:
#         integer_tip = int(tip)
#         total_tip = integer_tip / 100
#         final_bill = float(bill)
#         percent_bill = total_tip * final_bill
#         total_final_bill = final_bill + percent_bill
#         split = input("How many people to split the bill?: ")
#         people = int(split)
#         print("Each person should pay: " + "$" + str("{:.2f}".format(total_final_bill / people, 2)))
# else:
#     print("not valid")


number = input("Type in an even number: ")
if number % 2 == 0:
    print("This is an even number")
else: 
    print("This is an odd number")

