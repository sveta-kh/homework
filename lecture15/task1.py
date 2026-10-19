#Favourite author

def save_quotes():
    author = input("What is your favourit author? ")
    quote = input ("Please write his quote: ")
    with open("quotes.txt", "a") as file:
        file.write(f"{author}: {quote}\n")

save_quotes()


def read_quotes():
    with open ("quotes.txt", "r") as file:
        text = file.read()

        print(text)

read_quotes()
