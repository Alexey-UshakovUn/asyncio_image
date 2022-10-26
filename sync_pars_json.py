import requests
from time import time
import json

access_key = 'YBPmmoO0O8HH8DVHJG9UNf2NDQQSVxnQ6t8if_-VQgQ'
secret_key = 'Mu176dW5FR0tR-1SjIuaeN-y-HVcsjW1fnqLcERKESg'


def get_file(url: str):
    r = requests.get(url, allow_redirects=True)
    return r


def to_json(response: requests.models.Response):
    data = response.content.decode()  # bytes - > str
    data = json.loads(data)  # str - > list
    data = data[0]  # list -> dict
    data = json.dumps(data, indent=4)  # Переводим dict -> json
    return data


def write_file(data):
    filename = json.loads(data)['id']
    with open(filename, 'wt') as file:
        file.write(data)


def main():
    time_start = time()
    url = 'https://api.unsplash.com/photos/random?orientation=landscape&count=1&client_id={}'.format(access_key)
    for i in range(5):
        write_file(to_json(get_file(url)))

    print(time() - time_start)


if __name__ == '__main__':
    main()
