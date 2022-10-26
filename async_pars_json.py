from time import time
import json
import asyncio
import aiohttp

access_key = 'YBPmmoO0O8HH8DVHJG9UNf2NDQQSVxnQ6t8if_-VQgQ'
secret_key = 'Mu176dW5FR0tR-1SjIuaeN-y-HVcsjW1fnqLcERKESg'


async def get_file(url: str, session: aiohttp.client.ClientSession):
    async with session.get(url) as response:
        data = await response.json()
        data = data[0]  # list -> dict
        data = json.dumps(data, indent=4)  # Переводим dict -> json
        return data


def write_file(data):
    filename = json.loads(data)['id']
    with open(filename, 'wt') as file:
        file.write(data)


async def main():
    url = 'https://api.unsplash.com/photos/random?orientation=landscape&count=1&client_id={}'.format(access_key)
    async with aiohttp.ClientSession() as session:
        for i in range(5):
            data = await get_file(url, session)
            write_file(data)


if __name__ == '__main__':
    time_start = time()
    asyncio.run(main())
    print(time() - time_start)
