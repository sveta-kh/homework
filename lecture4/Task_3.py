#Smart ATM Cash Withdrawal

correct_pin = 1234
balance = 100000.0

entered_pin = int(input("Enter your pin: "))

if entered_pin == correct_pin:
    requested_amount = float(input("Enter amount: "))
    if requested_amount <= balance:
        balance = balance - requested_amount
        print(f"withdrawal successful! Remaining balance: ${balance}")
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")
