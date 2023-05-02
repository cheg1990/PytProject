from DataLoader import DataLoader
from DataAnalyze import DataAnalyze
from Dataview import DataView
from FILEHANDLER import FileHandler

def main():
    loader = DataLoader() #создаем переменную типа DataLoader
    loader.download_file('https://lk.globtelecom.ru/upload/test_prog1.csv') # при помощи метода скачиваем файл и записываем его в переменную
    data=loader.read_file() # передавая переменную с файлом, раскодируем и раксодированный файл записываем в переменную
    analyzer = DataAnalyze(data) # создаем переменную типо Dataanalyze передавая раскодированный файл
    view = DataView(analyzer) # создаем переменную типа DataView , передавая переменную типа Dataanalyze
    view.show_duplicate_phone_numbers()
    view.show_same_surname_count()
    view.show_age_stats() # вызываем методы переменной DataView, для отображения статистики
    record_to_file=FileHandler(data) # создаем переменную типо FileHandler, передавая раскодированный файл
    record_to_file.sort_file(data) # метод сортироваки инофрмации по файлам
    loader.delete_file() # удаляем скачанный файл


if __name__ == '__main__':
    main()
