import threading, time, requests

def fetch_info(post_id):
    BASE_URL = 'https://jsonplaceholder.typicode.com/posts/{id}'

    response = requests.get(BASE_URL.format(id=post_id), timeout=10)
    return response.json()

start =time.time()
thread_list = []

for i in range (1, 101):
    thread = threading.Thread(target=fetch_info, args=(i,))
    thread_list.append(thread)
for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end = time.time()

print(f"Total time taken: {end - start:.2f}")
    

