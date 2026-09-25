#Sum of Even Numbers
#####################

n = int(input("Enter any positive number: "))

total = 0

for i in range(2, n + 1, 2):
    total += i
print(f"The sum of even number from 1 to {n} is {total}")

