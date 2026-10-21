#Titanic Survived People

import csv

def filtered_passengers():
    try:
        with open ("titanic.csv", "r") as file:
            reader = csv.DictReader(file, delimiter= ",")

            survived_pasengrs = []
            for row in reader:
                if row["Survived"] == "1":
                    survived_pasengrs.append (row)

    except FileNotFoundError:
        print("File not found")
        return None
    
    return survived_pasengrs, reader.fieldnames            


def survivors(passengers, fieldnames):
    with open ("survived.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=",")

        writer.writeheader()
        writer.writerows(passengers)

result = filtered_passengers()

if result is not None:
    passengers, fieldnames = result
    survivors(passengers, fieldnames)


    

