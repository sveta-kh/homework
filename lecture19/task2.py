#Web Usernames

def users():
    visitors = ["Gio", "Nino", "Gio", "Ana", "Nika", "Ana"]
    unique = set(visitors)
    return unique

unique_visitors = users()
print(unique_visitors)
print(len(unique_visitors))



