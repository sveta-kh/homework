import asyncio, aiohttp

async def fetch_data_async(session, url):
    async with session.get(url) as response:
        return await response.json()

async def async_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range (1, 21):
            url = f"https://jsonplaceholder.typicode.com/posts/{i}"
            tasks.append(fetch_data_async(session, url))
        post = await asyncio.gather(*tasks)

        for i in post:
            if i["userId"] == 1:
                print(i["title"])

 
asyncio.run(async_requests())          