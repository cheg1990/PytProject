import csv
import re
import urllib.request
from datetime import datetime
import charset_normalizer
from prettytable import PrettyTable
from collections import Counter
import os


def download_file():
    url = "https://lk.globtelecom.ru/upload/test_prog1.csv"
    filename = "test_prog1.csv"
    urllib.request.urlretrieve(url, filename)


def d_encoding(filepath: str) -> str:
    with open(filepath, 'rb') as f:
        result = charset_normalizer.detect(f.read())
        return result.get('encoding')


def right_tel_num(line: str) -> bool:
    pattern = r"^[0-9]+$"
    if len(line) == 11 and re.match(pattern, line) :
        return True
    else:
        return False


def current_age(dob_str: str):
    dob = datetime.strptime(dob_str, "%d.%m.%Y")
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def table_view(column1=0,record1=0,column2=0,record2=0):
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

def same_phone():
    filepath = './test_prog1.csv'
    encoding = d_encoding(filepath)
    with open(filepath, 'r', encoding=encoding) as f:
        phones = []
        for line in f:
            phone = line.strip().split(';')[0]
            phones.append(phone)
        duplicate_phones = set([phone for phone in phones if phones.count(phone) > 1])
        num_duplicate_phones = len(duplicate_phones)
        table_view("Количество повторяющихся номеров телефона", num_duplicate_phones, "Повторяющиися номера",duplicate_phones)

def same_surname():
    filepath = './test_prog1.csv'
    encoding = d_encoding(filepath)
    with open(filepath, 'r', encoding=encoding) as f:
        surnames = []
        for line in f:
            surname = line.split()[4]
            surnames.append(surname)
        surname_counts = Counter(surnames)
        samesurname_count = 0
        for surname, count in surname_counts.items():
            if count > 1:
                samesurname_count += count
        print(samesurname_count)
        table_view("Количество однофамильцев", samesurname_count)

def stats_ages():
    filepath = './test_prog1.csv'
    encoding = d_encoding(filepath)
    with open(filepath, 'r', encoding=encoding) as f:
        years = {}
        for line in f:
            date_string = line.strip().split(';')[8]
            date_obj = datetime.strptime(date_string, "%d.%m.%Y")
            year = date_obj.year
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
        print("Статистика по годам рождения:")
        for year, count in sorted(years.items()):
            count = years[year]
            table_view("Год", year, "Количество", count)

def stats():
    same_phone()
    same_surname()
    stats_ages()

def format(initials,tel,date_of_birth,age):
    return f'ФИО: {initials};Телефон : {tel};Дата Рождения: {date_of_birth};Возраст на сегодня:{current_age(age)};\n'


def sort_file():
    filepath = './test_prog1.csv'
    encoding = d_encoding(filepath)
    with open(filepath, 'r', encoding=encoding) as f:
        reader = csv.reader(f, delimiter=';')
        for i,line in enumerate(reader):
            if right_tel_num(line[0]) == False:
                wrong_string=f'{i};ИО : {line[3]};Телефон : {line[0]};\n'
                print(wrong_string)
            if right_tel_num(line[0]) and line[7] == 'pos':
                right_string = format(line[4],line[0],line[8],line[8])
                with open("pos_h.csv", "a", encoding=encoding) as f:
                    f.write(right_string)
            if right_tel_num(line[0]) and line[7] == 'cash':
                right_string = format(line[4],line[0],line[8],line[8])
                with open("cash_h.csv", "a", encoding=encoding) as f:
                    f.write(right_string)

def delete_url():
    filepath = './test_prog1.csv'
    os.remove(filepath)


def main():
    download_file()
    sort_file()
    stats()
    delete_url()


if __name__ == '__main__':
    main()
