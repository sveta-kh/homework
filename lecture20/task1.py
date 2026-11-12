#Task 1 - Dataclass
import json
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

product1 = Product("Laptop", 2500.0, True)
product2 = Product("Mobile Phone", 1500.0, True)
product3 = Product("HDD", 700.0, True)

print(product1)
print(product2)
print(product3)

#Task 2 -Serialization

product1_dict = asdict(product1)
product2_dict = asdict(product2)
product3_dict = asdict(product3)
products = [product1_dict, 
            product2_dict, 
            product3_dict
            ]
print(products)

json_products = json.dumps(products, indent=4)
print(json_products)

#task 3 Deserialization

json_text = '{"name": "Laptop", "price": 2500, "in_stock": true}'
python_data = json.loads(json_text)
print(python_data)

p = Product(**python_data)
print(p)