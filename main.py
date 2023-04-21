import os
from DataLoader import DataLoader
from DataAnalyze import DataAnalyze
from Dataview import DataView
from FILEHANDLER import FileHandler

def main():
    loader = DataLoader('https://lk.globtelecom.ru/upload/test_prog1.csv') #создаем переменную типа DataLoader, передавая ссылку
    filepath = loader.download_file() # при помощи метода скачиваем файл и записываем его в переменную
    data=loader.read_file(filepath) # передавая переменную с файлом, раскодируем и раксодированный файл записываем в переменную
    analyzer = DataAnalyze(data) # создаем переменную типо Dataanalyze передавая раскодированный файл
    view = DataView(analyzer) # создаем переменную типа DataView , передавая переменную типа Dataanalyze
    view.show_duplicate_phone_numbers()
    view.show_same_surname_count()
    view.show_age_stats() # вызываем методы переменной DataView, для отображения статистики
    record_to_file=FileHandler(data) # создаем переменную типо FileHandler, передавая раскодированный файл
    record_to_file.sort_file(data) # метод сортироваки инофрмации по файлам
    os.remove(filepath) # удаляем скачанный файл


if __name__ == '__main__':
    main()
