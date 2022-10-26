import asyncio
import aiohttp
from time import time


async def get_file(url: str, session: aiohttp.client.ClientSession) -> None:
    async with session.get(url) as response:
        data = await response.read()
        write_image(data)


def write_image(data: bytes) -> None:
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def main() -> None:
    url = 'https://loremflickr.com/640/360'

    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(get_file(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    time_start = time()
    asyncio.run(main())
    print(time() - time_start)
