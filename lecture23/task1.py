import requests, time, asyncio, aiohttp

def fetch_data(url):
    response = requests.get(url, timeout=10)
    return response.json()

def seq_request():
    start = time.time()

    for i in range(1, 11):
        url = f"https://jsonplaceholder.typicode.com/todos/{i}"
        fetch_data(url)
    end = time.time()
    print(f"Sequential time: {end-start:.2f}") 

seq_request()

#Asyncio
async def fetch_data_async(session, url):
    async with session.get(url) as response:
        return await response.json()

async def async_requests():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range (1, 11):
            url = f"https://jsonplaceholder.typicode.com/todos/{i}"
            tasks.append(fetch_data_async(session, url))
        await asyncio.gather(*tasks)
    end = time.time()
    print(f"Async time: {end-start:.2f}")  
asyncio.run(async_requests())          