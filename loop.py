friends = ["Dami", "AK", "Orobosa", "Tomisin"]
for friend in friends:
    print(friend + " " + "is a good friend")

ca = 23
scores = [61, 53, 67, 64, 59]
for score in scores:
    score += ca
    print(score)

val = 3

print(val)

max_score = 0
scores = [61, 53, 67, 64, 59]

for score in scores:
       max_score += score

print(max_score)

constant = 0
for number in range(1, 101):
    constant += number
print(constant)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        

