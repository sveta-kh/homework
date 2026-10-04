# Nested Dictionary Extraction & Update

student = {"name": "Ana", 
           "age": 20, 
           "contacts": {
               "email": "ana@example.com", 
                "phone": "599123456"
           },
           "courses": {
               "python": {"scores": 95, "passed": True},
               "web": {"scores": 58, "passed": False}
           }    
}

print(student ["contacts"] ["email"])
print(student ["courses"] ["python"] ["scores"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["scores"] = 65

del student["contacts"]["phone"]

print(student)

