# testing out print functions
print("Hello World!")
print("I am Pascal")

num1 = input("What was your math score?: ")
num2 = input("What was your chemistry score?: ")
print(num1 + num2)

# using quotes insside a print quote requires alternating the quotes between single and double quotes.
print('She said: "Hello" and then left.')
# # Another way would be to place the escape back slash in front of the two interior double quotes
# # as a way to tell the computer to ignore it as a code and just print it the way you intend. for example:

print("She said: \"Hello\" and then left.")
# # now, to test them:
# # A 'single quote' inside a double quote
# A "double quote" inside a single quote
#Alternatively, you can just \"escape\" the quote"

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively, you can just \"escape\" the quote")

# # How to create a new line using the backslash-n \n

print("Hello world!\nHello world!\nHello world!")

# # combining two strings
print("Hello" + " Pascal")
print("Hello" + " " + "Pascal")

# Python input function
# for the input function, the string in the parenthesis is called a prompt. 
name = input("What is your name?: ")
print("Hello", name)
# Another way I can achieve this is by nesting the input function with hello:
print("Hello " + input("What is your name?: "))
# For the above line, python first executes the input function then passes the answer into the print function altogether.


# using the if and is.digit function to filter out strings from values in the prompt
age = input("How old are you?: ")

if age.isdigit():
    if age >= "30":
        print("Wow, you are", age + "?", "that's quite old, ngl")
    elif age < "30":
        print("You are young, that is nice!")
else:
    print("That was not what I asked you for dork!")

# the len function can be used to get the number of characters in a string or the number of strings in a collection
print(len("Hello"))
surname = "Onaho"
print(len(surname))

name = input("What is your name?: ")
length = len(name)
print(length)

# Band Name Generator
print("Welcome to the Band Name Generator.")
city_name = input("what is the name of the city's you grew up in?: \n")
pet_name = input("What is the name of your pet?: \n")
print("Your band name could be", city_name, pet_name)









