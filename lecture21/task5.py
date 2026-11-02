
import requests

BASE_URL = 'https://crudcrud.com/api/f26fe82063bc439eb05ac71a5471fc5e'

response = requests.delete(f'{BASE_URL}/products/6ae7ac4685e4dd03e8d42ba9', timeout=10)

print(response.status_code)

if response.status_code == 200:
    print("Product deleted successfully")
else:
    print("Delete failed: ", response.status_code)
        
