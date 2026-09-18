#booleans/bool
number = int(input("Enter a Number: "))
is_positive = number > 0
is_negative = number < 0
is_zero = number == 0
is_even = number % 2 == 0
is_odd = number % 2 != 0
print ("Positive", is_positive)
print ("Negative", is_negative)
print ("Zero", is_zero)
print ("Even", is_even)
print ("Odd", is_odd)
