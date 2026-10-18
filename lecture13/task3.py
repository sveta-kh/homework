#Greeter Bot

def greeter_bot():
    name = yield "Enter your name"
    while True:
        name = yield (f"Hallo, {name}!")

greet = greeter_bot()

print(next(greet))
print(greet.send("Anna"))
print(greet.send("Luka"))



