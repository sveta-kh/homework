import requests

BASE_URL = 'https://crudcrud.com/api/f26fe82063bc439eb05ac71a5471fc5e'

response = requests.get(f"{BASE_URL}/products", timeout=10)

for item in response.json():
    print(item["name"], item["price"], item["_id"])
