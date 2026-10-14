#Execution Counter Closure 

def make_counter(start_value = 0):
    
    def counter():
        nonlocal start_value
        start_value +=1
        return start_value
    return counter

counter = make_counter(start_value = 10)

print(counter())
print(counter())


