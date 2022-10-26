import requests
from time import time


def parse_page(url: str):
    r = requests.get(url)
    data = r.text
    return data


def get_url_image(data: str):
    if "id=\"cat" in data:
        url_image = data.split("src=\"")[1].split('\"')[0]
    else:
        url_image = None
        print('Wrong random')
    return url_image


def get_file(url_image):
    r = requests.get(url_image)
    filename = 'cats/' + r.url.split('/')[-1]
    with open(filename, 'wb+') as file:
        file.write(r.content)


if __name__ == '__main__':
    start_time = time()
    url = 'https://aws.random.cat/'

    for _ in range(5):
        page = parse_page(url)
        url_image = get_url_image(page)
        get_file(url_image)

    print(time() - start_time)
