
import requests

BASE_URL = 'https://crudcrud.com/api/f26fe82063bc439eb05ac71a5471fc5e'

update_product = {
    "name": "Gaming Laptop", 
    "price": 2500, 
    "in_stock": True
}

response = requests.put(f'{BASE_URL}/products/6ae7ac4685e4dd03e8d42ba9', json=update_product, timeout=10)

print(response.status_code)


