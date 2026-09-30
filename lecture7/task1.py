#Shopping Cart Total & Price Parser

try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter Quantity: "))
    total = price * quantity

except ValueError:
    print("Error: Both price and quantity must be valid numbers!")

else:
    print(f"Total price: ${total:.2f}")
        