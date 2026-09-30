#Safe List Index Accessor

fruits = ["apple", "banana", "cherry", "orange"]

try:
    index = int(input("Enter index number: "))
    print(f"Selected fruit: {fruits[index]}")

except ValueError:
    print("nvalid input! Please enter a whole number.")

except IndexError:
    print(f"ndex out of bounds! Choose an index between 0 and {len(fruits)-1}.")

else:
    print("Successfully retrieved item!")
    