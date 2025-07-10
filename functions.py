# Create a function where you have to give ticket discount to customers above 30 years old for a rollercoaster
# Customers below 18 won't be allowed to ride. Those from 18 to 29 will pay 50 dollars
# Those credible for a discount would pay 70% of the total fees of 50 dollars.

#Step 1: Select for credible and non-credible participants

age = int(input("How old are you?\n"))
discount = int(50/1.3)
price = 50
if age >= 18:
    print("You can proceed to pay for this rollercoaster!")
    if age >= 30:
        print(f"You have been given a discount of 30%.\nPlease proceed to pay ${discount}")
    else:
        print(f"You are required to pay ${price}")
else:
    print("You are not eligible to get on this rollercoaster!")
