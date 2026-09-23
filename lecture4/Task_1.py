#Smart Movie Theater Ticket Pricing
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age enetered")
elif age <= 4:
    print("Your ticket price is $0")
elif age <=12:
    print("Your ticket price is $8")
elif age <=64:
    print("Your ticket prise is $15")
else:
    print("Your ticket price is $10")

