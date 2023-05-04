import urllib.request
import charset_normalizer
import os

class DataLoader:
    def __init__(self):
        self.url = None
        self.filename = None
        self.content = None

    def download_file(self, url):
        self.url = url
        self.filename = 'test_prog1.csv'
        urllib.request.urlretrieve(self.url, self.filename)


    def get_encoding(self):
        with open(self.filename, 'rb') as f:
            result = charset_normalizer.detect(f.read())
            return result.get('encoding')

    def read_file(self):
        encoding = self.get_encoding()
        with open(self.filename, 'r', encoding=encoding) as f:
            data = f.read()
            data = [line for line in data.split('\n') if line.rstrip()] # разбиваем файл на строки и удаляем пустые строки.
            sorted_data = sorted(data, key=lambda x: tuple(x.split(';')[i] for i in (0, 3, 4, 7, 8))) # проводим сортировку данных
            self.content = [(s.split(';')[0], s.split(';')[3], s.split(';')[4], s.split(';')[7], s.split(';')[8]) for
                              s in sorted_data] # Для каждой строки, полученной после сортировки, берем нужные нам данные и записываем их в виде кортежа
            return self.content

    def delete_file(self):
        os.remove(self.filename)
