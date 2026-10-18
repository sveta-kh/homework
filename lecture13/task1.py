#Infinite Even Numbers

def even_numbers():
    num = 0
    while True:
        yield num
        num +=2

func = even_numbers()

for num in func:
    print(num)
    if num == 18:
        break
    
