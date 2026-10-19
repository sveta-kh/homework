#ssl_companies

import csv

def all_companies():
    
    with open("ssl_companies.csv", "r") as file:
        reader = csv.DictReader(file, delimiter= ",")

        big_companies = []
            
        for row in reader:
            if int(row["Number of employees"]) > 1000:
                companies = {"Name": row["Name"], "Industry": row["Industry"], "Number of employees": ["Number of employees"]}
                big_companies.append(companies)

    return big_companies            

def sorted_companies(companies):

    fieldnames = ["Name", "Industry", "Number of employees"]
        
    with open("sorted_companies.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter="," )

        writer.writeheader()
        writer.writerows(companies)

try:
    result= all_companies()
    sorted_companies(result)

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Incorrect Value")
    






