#User Profile

class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(self.username)
        print(self.email)
        print(self.age)

user1 = User("Sofie", "sofi@gmail.com", 25)
user1.get_info()

user2 = User("Giorgi", "gio@gmail.com", 27)
user2.get_info()

print(User.status)
