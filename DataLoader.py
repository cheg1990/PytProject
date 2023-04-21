import urllib.request
import charset_normalizer

class DataLoader:
    def __init__(self, url):
        self.url = url

    def download_file(self):
        urllib.request.urlretrieve(self.url, 'test_prog1.csv')
        filename = 'test_prog1.csv'
        return filename

    def get_encoding(self, file_path):
        with open(file_path, 'rb') as f:
            result = charset_normalizer.detect(f.read())
            return result.get('encoding')

    def read_file(self, file_path):
        encoding = self.get_encoding(file_path)
        with open(file_path, 'r', encoding=encoding) as f:
            data = f.read()
        return data.split('\n')
