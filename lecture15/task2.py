#Titanic Survived People

import csv

def filtered_passengers():

    with open ("titanic.csv", "r") as file:
        reader = csv.DictReader(file, delimiter= ",")

        survived_pasengrs = []
        for row in reader:
            if row["Survived"] == "1":
                survived_pasengrs.append (row)
    return survived_pasengrs, reader.fieldnames            


def survivors(passengers, fieldnames):
    with open ("survived.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=",")

        writer.writeheader()
        writer.writerows(passengers)

try:
    pasengers, fieldnames = filtered_passengers()
    survivors(pasengers, fieldnames)

except FileNotFoundError:
    print("File not found")




    

