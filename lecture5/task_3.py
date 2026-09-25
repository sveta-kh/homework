#Text Filter — Skip Digits
###########################


text = input("Enter text: ")

for num in text:
    if num.isdigit():
        continue
    print(num, end="")
