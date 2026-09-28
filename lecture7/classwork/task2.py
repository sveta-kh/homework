#Password Validator

try:
    password = input("Enter Your Password: ")
    if len(password) < 6:
        raise ValueError ("Password is too short!")
    
except ValueError as e:
    print(e)
