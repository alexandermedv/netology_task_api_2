import requests

hulk_url = "https://superheroapi.com/api/2619421814940190/search/hulk"
lis = requests.get(hulk_url).json()['results']


class YaUploader:
    def __init__(self, file_list):
        self.file_list = file_list

    def upload(self):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        # Вставьте свой токен:
        token = ''
        headers = {"Authorization": token}

        for file_path in self.file_list:
            params = {"path": file_path}
            resp = requests.get(url, headers=headers, params=params)
            print(resp.json())

            with open(file_path, 'rb') as f:
                print('Загрузка файла:', file_path)
                response = requests.post(resp.json()['href'], files={"file": f})
                print(str(response))
                if str(response) == '<Response [201]>':
                    print('Файл успешно загружен')
                else:
                    return 'Файл не загружен'

        return 'Загрузка выполнена'


if __name__ == '__main__':
    uploader = YaUploader(["Файл для загрузки 1.txt", "Файл для загрузки 2.txt"])
    result = uploader.upload()
    print(result)
