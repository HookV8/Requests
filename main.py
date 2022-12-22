import requests


def get_intelligens(name):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    for hero in response:
        if hero['name'] == name:
            return hero['powerstats']['intelligence']


def SH_Choice():
    heroes = ['Hulk', 'Captain America', 'Thanos']
    rating_list = []
    for n in heroes:
        rating_list.append([get_intelligens(n), n])
    rating_list.sort(reverse=True)
    return f'{rating_list[0][1]} - это самый умный супергерой среди: {", ".join(heroes)}\n' \
           f'Его уровень интеллекта {rating_list[0][0]} единиц'


print(SH_Choice())


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file):

        upload_link = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload',
                                   headers={'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'},
                                   params={'path': path_to_file}
                                   )
        response = requests.put(upload_link.json()['href'],
                                headers={'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'},
                                data=open(path_to_file, 'rb')
                                )

        print(response.status_code)
        if response.status_code == 200 or 201:
            print('Загрузка прошла успешно')




if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
