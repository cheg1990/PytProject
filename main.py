import csv
import re
import urllib.request
from datetime import datetime
import charset_normalizer
from prettytable import PrettyTable
from collections import Counter
import os

def download_file():  #скачиваем файл
    url = 'https://lk.globtelecom.ru/upload/test_prog1.csv'
    filename = 'test_prog1.csv'
    urllib.request.urlretrieve(url, filename)
    return filename

FILEPATH = download_file() # задаем константу, не уверен, что так вообще принято, посередине код)

def d_encoding(FILEPATH: str) -> str: #раскодируем полученный файл
    with open(FILEPATH, 'rb') as f:
        result = charset_normalizer.detect(f.read())
        return result.get('encoding')

def read_file(): #считываем созержимую файла, позже в main прсивоим к переменной, разделяем строки по \n
    encoding = d_encoding(FILEPATH)
    with open(FILEPATH, 'r', encoding=encoding) as f:
        data = f.read()
    return data.split('\n')

def right_tel_num(line: str) -> bool: #удаляем лишние знаки и проверяем что в номере 11 цифр
    pattern = r'\D+'
    digits_only = re.sub(pattern, '', line)
    if len(digits_only) == 11:
        return True
    else:
        return False


def current_age(dob_str: str): #функция для расчета текущего возраста
    dob = datetime.strptime(dob_str, '%d.%m.%Y')
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def table_view(column1=0,record1=0,column2=0,record2=0): #функция для таблицы
    if column2==0 and record2==0:
        table = PrettyTable()
        table.field_names = [column1]
        table.add_row([record1])
        print(table)
    else:
        table = PrettyTable()
        table.field_names = [column1, column2]
        table.add_row([record1, record2])
        print(table)

def same_phone(data): #проверка одинковых номеров телефонов
    phones = []
    for line in data:
        phone = line.strip().split(';')[0]
        phones.append(phone)
    duplicate_phones = set([phone for phone in phones if phones.count(phone) > 1])
    num_duplicate_phones = len(duplicate_phones)
    table_view('Количество повторяющихся номеров телефона', num_duplicate_phones, 'Повторяющиися номера',duplicate_phones)

def same_surname(data): #проверка однофамильцев, их оказывается много - предыдущий раз функция не работала
    surnames = []
    for line in data:
        fields = line.split(';')
        if len(fields) >= 5:  #если не задать этот if (что в строке больше 5 ';' - какие-то строки почему-то не читает правильно. Не смог разобраться.
            full_name = fields[4].strip()  # убираем лишние пробелы в начале и конце
            surname = full_name.split()[0]  # извлекаем первое слово (фамилию)
        surnames.append(surname)
    surname_counts = Counter(surnames)
    samesurname_count = 0
    for surname, count in surname_counts.items():
        if count > 1:
            samesurname_count += count
    table_view('Количество однофамильцев', samesurname_count)

def stats_ages(data): # функция для статистики по годам
    years = {}
    for line in data:
        fields = line.split(';')
        if len(fields) >= 8:
            date_string = fields[8].strip()
        date_obj = datetime.strptime(date_string, '%d.%m.%Y')
        year = date_obj.year
        if year in years:
            years[year] += 1
        else:
            years[year] = 1
    print('Статистика по годам рождения:')
    table = PrettyTable()
    table.field_names = ['Год', 'Количество'] #из-за того, что надо передать две переменные в цикле, а две нет, предыдущая функция table_view не особо подходит. Тоже не смог разобраться, как сделать, чтобы вот такая нормальная таблица выходила.
    for year, count in sorted(years.items()):
        count = years[year]
        table.add_row([year, count])
    print(table)

def format(initials,tel,date_of_birth,age): #функция для формата записи в файл
    return f'ФИО: {initials};Телефон : {tel};Дата Рождения: {date_of_birth};Возраст на сегодня:{current_age(age)};\n'


def write_in_file(name_of_file,string_to_write): #функция записи в файл
    with open(name_of_file, 'a', encoding='utf-8') as f:
        f.write(string_to_write)

def sort_file(data): #функция сортировки по файлам
    lines = '\n'.join(data)
    for i,line in enumerate(lines.split('\n')):
        cells = line.split(';')
        if len(cells) < 9: #аналогично, тому где условие > 5 ';'
            continue
        tel_num = cells[0]
        name = cells[3]
        full_name = cells[4]
        date_of_birth = cells[8]
        type_of_payment = cells[7]  #присваиваем значения строк к переменным
        number_corr=right_tel_num(tel_num)
        right_string = format(full_name, tel_num, date_of_birth, date_of_birth)
        if number_corr == False:
            wrong_string=f'{i};ИО : {name};Телефон : {tel_num};\n'
            print(wrong_string)
        if number_corr and type_of_payment == 'pos':
            write_in_file('pos_h.csv',right_string)
        if number_corr and type_of_payment == 'cash':
            write_in_file('cash_h.csv', right_string)

def delete_url(): #удаление файла
    os.remove(FILEPATH)

def main():
    data = read_file() #присваиваем считанный файл к переменной
    download_file()
    sort_file(data)
    same_phone(data)
    same_surname(data)
    stats_ages(data)
    delete_url()


if __name__ == '__main__':
    main()
