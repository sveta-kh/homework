#Secret PIN Code
##################

pin = ""
tries = 0

while pin != "1234" and tries < 3:
    pin = input("Enter Your PIN: ")
    if pin == "1234":
        print("Access granted!")
        break
    tries += 1
    remaining_tries = 3 - tries

    if tries < 3:
        print(f"Incorrect PIN. Remaining attempts: {remaining_tries}")
    else:
        print("Card blocked!")


