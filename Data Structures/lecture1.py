final_names = ""
names = ["Pascal", "Obodo", "Aj", "Paulus", "Hannah", "Juliet", "Catherine"]
for name in names:
    final_names += name + " "

print(final_names)

for i in range(0, 7):
    for j in range(i + 1):
        print(names[i]) #this prints the items in increasing number
    
    print(i) #this prints the index positions
    print(names[i]) #this prints the individual item in the list according to its index


number =int(input("Wite down a number:\n"))

if number%3 == 0 and number%5 == 0:
    print("Correct")
else:
    print("Incorrect")


arithmetic = list(range(1, 100))
final_sum = []
for number in arithmetic:
    if number%3 == 0 or number%5 == 0:
        final_sum.append(number)
print(sum(final_sum))

given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

var = []

for item in given_list:
    if item < 0:
        var.append(item)
print(sum(var))  


secret = 5

secret_number = None

while True:
     secret_number = int(input("Guess a number between 1 and 10: "))

     if secret_number == secret:
          print("You are correct!")
          break
     else:
          print(" Try again.")
ill = "sickle"
ill = list(ill)
for letter in ill:
     print (letter)


     

    
