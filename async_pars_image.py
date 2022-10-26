import aiohttp
import asyncio
from time import time


async def parse_page(url: str, session: aiohttp.client.ClientSession):
    async with session.get(url) as response:
        data = await response.text()
        return data


def get_url_image(data: str):
    if "id=\"cat" in data:
        url_image = data.split("src=\"")[1].split('\"')[0]
    else:
        url_image = None
        print('Wrong random')
    return url_image


async def get_file(url_image: str, session: aiohttp.client.ClientSession):
    async with session.get(url_image) as response:
        data = await response.read()
        filename = 'cats/' + response.url.name.split('/')[-1]
        with open(filename, 'wb+') as file:
            file.write(data)


async def main():
    url = 'https://aws.random.cat/'
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(5):
            data = await parse_page(url, session)
            url_image = get_url_image(data)
            task = asyncio.create_task(get_file(url_image, session))
            tasks.append(task)
        await asyncio.gather(*tasks)

start_time = time()
asyncio.run(main())
print(time() - start_time)