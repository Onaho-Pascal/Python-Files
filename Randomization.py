import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)


heads = 0
tails = 1
coin_flip = random.randint(0, 1)
if coin_flip == 0:
    print("Heads")
else:
     print("Tails")


#Lists

states_in_nigeria = ["Abia", "Adamawa", "Akwa-ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross-river", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu"]

print(states_in_nigeria[2])
print(states_in_nigeria[4])

# Negative indexing starts from behind
states_in_nigeria.append("Gombe")
print(states_in_nigeria)

print(states_in_nigeria[-1])

states_in_nigeria.append("Jigawa")
print(states_in_nigeria)

#To extend a list, we have to use the extend function

states_in_nigeria.extend(["Kaduna", "Kano", "Kastina", "Kebbi", "Kogi"])

print(states_in_nigeria)


# to randomly decide who pays the bills

bill_payer = ["uche", "chimsom", "pascal", "David", "fafa", "Oge"]

food = len(bill_payer)
pay =random.randint(0, food - 1)
print(bill_payer[pay])
