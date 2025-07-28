# final_names = ""
# names = ["Pascal", "Obodo", "Aj", "Paulus", "Hannah", "Juliet", "Catherine"]
# for name in names:
#     final_names += name + " "

# print(final_names)

# for i in range(0, 7):
#     for j in range(i + 1):
#         print(names[i]) #this prints the items in increasing number
    
#     print(i) #this prints the index positions
#     print(names[i]) #this prints the individual item in the list according to its index


# # number =int(input("Wite down a number:\n"))

# # if number%3 == 0 and number%5 == 0:
# #     print("Correct")
# # else:
# #     print("Incorrect")


# # arithmetic = list(range(1, 100))
# # final_sum = []
# # for number in arithmetic:
# #     if number%3 == 0 or number%5 == 0:
# #         final_sum.append(number)
# # print(sum(final_sum))

# # given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

# # var = []

# # for item in given_list:
# #     if item < 0:
# #         var.append(item)
# # print(sum(var))  


# # secret = 5

# # secret_number = None

# # while True:
# #      secret_number = int(input("Guess a number between 1 and 10: "))

# #      if secret_number == secret:
# #           print("You are correct!")
# #           break
# #      else:
# #           print(" Try again.")
# # ill = "sickle"
# # ill = list(ill)
# # for letter in ill:
# #      print (letter)

# list = ["veteran", "learn", "aspect", "dog", "purse", "detail", "monster", "trouble", "industry", "mouse", "attitude", "document"]
     

    
# given_list = [5, 4, 3, -2, 1, -1, -2, -3]

# final_number = 0

# for number in given_list:
#     if number > 0:
#         final_number += number
#     # else:
#     #     break    
# print(final_number)

# import keyword
# print(keyword.kwlist)

# def my_function():
#     a = 50
#     return a
# print(my_function())

# i = 7
# if isinstance(i, int):
#     i += 1
# elif isinstance(i, str):
#     i = int(i)
#     i += 1
# print(i)

# y = [1, 4, 7]
# def f(m):
#     m.append(3)
#     return m


# print(f(y))

# professions = ["Pharmacy", "Bioinformatician", "Chemist", "Doctor", "Lawyer"]

# numbers = [1, 2, 3, 4, 5]

# # for number in numbers:
# #     profession.append(number)
# # print(profession)

# print(numbers.count(2))


# Continents = {
#     "Africa": ["NIgeria", "Ghana", "Kenya"],
#     "North America": ["Canada", "USA", "Mexico"],
#     "South America": ["Brazil", "Colombia", "Cuba"]
# }

# for continent in Continents.keys():
#     print("{} are countries in {}".format(Continents[continent], continent))



import class_tutorial

#print(class_tutorial.entry("Pascal"))

Pascal = 16

#print(class_tutorial.gate_fee(Pascal))


wosan = list(range(1, 11))
init = 0



#print(class_tutorial.mean(wosan, init))

score = 100

#print(class_tutorial.calculate_grade(score))


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    def average_grade(self):
        average_ = class_tutorial.mean(self.grades)
        return f"{self.name} had an average grade of {average_}"
    


#student_name = Student("Dominic", 23, [72, 69, 81, 84, 79])


nums = [3, 5, 7, 9, 11]

for i in nums:
    print(i)