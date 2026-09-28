#Age Calculator

try:
    birth_year = int(input("Enter Your Birth Year: "))
    age = 2026 - birth_year
    print("Your Age is: ", age)

except ValueError:
    print("Please enter only digits!")
    
    
    
