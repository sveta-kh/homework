#ssl_companies

import csv

def all_companies():

    big_companies = []

    try:
        with open("ssl_companies.csv", "r") as file:
            reader = csv.DictReader(file, delimiter= ",")
                
            for row in reader:
                if int(row["Number of employees"]) > 1000:
                    companies = {"Name": row["Name"], "Industry": row["Industry"], "Number of employees": row["Number of employees"]}
                    big_companies.append(companies)
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError:
            print("Incorrect Value") 
            return None      

    return big_companies            

def sorted_companies(companies):
        fieldnames = ["Name", "Industry", "Number of employees"]
            
        with open("sorted_companies.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames, delimiter="," )

            writer.writeheader()
            writer.writerows(companies)
            
            
result = all_companies()

if result is not None:
    sorted_companies(result)

         

    






