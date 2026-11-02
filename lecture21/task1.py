
import requests

BASE_URL = 'https://crudcrud.com/api/f26fe82063bc439eb05ac71a5471fc5e'

product = {
    "name": "Laptop",
    "price": 2500, 
    "in_stock": True
}

response = requests.post(f"{BASE_URL}/products", json=product, timeout=10)

print(response.json())

