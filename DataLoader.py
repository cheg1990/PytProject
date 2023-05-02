import urllib.request
import charset_normalizer
import os

class DataLoader:
    def __init__(self):
        self.url = None
        self.filename = None

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
            data = [line for line in data.split('\n') if line.rstrip()]
        return data

    def delete_file(self):
        os.remove(self.filename)
