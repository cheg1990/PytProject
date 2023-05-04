from DataLoader import DataLoader
from DataAnalyze import DataAnalyze
from Dataview import DataView
from FILEHANDLER import FileHandler


def main():
    loader = DataLoader() # создаем обЪект класса Dataloader
    loader.download_file('https://lk.globtelecom.ru/upload/test_prog1.csv') # передаем ссылку и скачиваем файл
    data = loader.read_file() # записываем в переменную, всю нужную информацию с файла
    analyzer = DataAnalyze(data) # создаем объект класса DataAnalyze
    view = DataView(analyzer) # создаем объект класса DataView и передаем объект класс DataAnalyze
    view.show_duplicate_phone_numbers()
    view.show_same_surname_count()
    view.show_age_stats() # выводим статистику
    file_handler = FileHandler(data) # создаем объект класса FileHandler
    file_handler.sort_file() # записываем информацию в файл
    loader.delete_file() # удаляю файл

if __name__ == '__main__':
    main()
