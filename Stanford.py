game = "Brawlhalla"
platform = "Playstation 4 or 5"

print("The name of the video game is {}, and you can play it on {}." .format(game, platform))

numbers = [1, 2, "three", 4, 5]
numbers[2] = 3 #replacing the value "three" with "3" in a list
numbers.append(6) #to add the number 6 to the list, I used the "append" function
print(numbers)

# "del" function can be used to delete an item from a list
del numbers[5]
print(numbers)


# When getting the sublist of a list, the colon ":" is used to get the range of sublist required
# This colon is separated by two index position of the list, with the end position being excluded

alphabets =  [1, 2, 3, 9, 15, 8]
subalphabets =  alphabets[0:4] # I expect a print out from a to 9

print(subalphabets)

print(alphabets[::-1]) #this prints out the entire list, but in reverse.

for item in alphabets:
    print(item + 2)

for  test in alphabets:
    print("{} multiplied by 2 is equal to {}." .format(test, test*2))

# Remember, in Python, the end of the range() is excluded.
# So the value 5 will not be included in the generated values.

for num in range(1, 5):
    print(num)


#The range() function generates a list of numbers, but the numbers don't have to be used within the for loop. 
# The list can be used simply as a counter, to perform a task a given number of times:

for num in range(1, 5):
    print("Looping...")

onaho = [2, 5, 6, 9, 13,14]

for item in onaho:
    print(onaho.append(item*2))