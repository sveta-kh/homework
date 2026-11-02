
import requests

BASE_URL = 'https://crudcrud.com/api/f26fe82063bc439eb05ac71a5471fc5e'

response = requests.get(f'{BASE_URL}/products/6ae7ac4685e4dd03e8d42ba9', timeout=10)
print(response.json())
