import requests
from time import time


def get_file(url: str):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response: requests.models.Response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    time_start = time()

    url = 'https://loremflickr.com/640/360'

    for i in range(10):
        write_file(get_file(url))

    print(time() - time_start)


if __name__ == '__main__':
    main()
