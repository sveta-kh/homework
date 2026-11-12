import threading, time, requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_info(post_id):
    BASE_URL = 'https://jsonplaceholder.typicode.com/posts/{id}'

    response = requests.get(BASE_URL.format(id=post_id), timeout=10)
    return response.json()

start =time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    result = list(executor.map(fetch_info, range(1, 101)))
end = time.time()

print(f"Map time: {end -start:.2f}")

start = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_url = {executor.submit(fetch_info, i): i for i in range(1, 101)}

    for future in as_completed(future_to_url):
        future.result()
end = time.time()

print(f"Submit time: {end - start:.2f}")