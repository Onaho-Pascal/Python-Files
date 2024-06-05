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

    
