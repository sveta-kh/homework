#Phone Dictionary

class PhoneBook:
    def __init__(self) -> None:
        self.contacts = {"Giorgi":"555111222", 
                         "Ana":"555222333", 
                         "Nika":"555123123", 
                         "Mariami":"551333444"
        }

    def find_contact(self):
        name = input("Enter a name: ")
        print(self.contacts.get(name, "Contact not found"))

contacts1 = PhoneBook()
contacts1.find_contact()

