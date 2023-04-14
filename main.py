import csv
import re
import urllib.request
from datetime import datetime
import charset_normalizer
from prettytable import PrettyTable
from collections import Counter
import os


def download():
    url = "https://lk.globtelecom.ru/upload/test_prog1.csv"
    filename = "test_prog1.csv"
    urllib.request.urlretrieve(url, filename)


def d_encoding(filepath: str) -> str:
    with open(filepath, 'rb') as f:
        result = charset_normalizer.detect(f.read())
        return result.get('encoding')


def right(line: str) -> bool:
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

def stats():
    filepath = './test_prog1.csv'
    encoding = d_encoding(filepath)
    with open(filepath, 'r', encoding=encoding) as f:
        phones = []
        surnames = []
        years = {}
        for line in f:
            phone = line.strip().split(';')[0]
            phones.append(phone)
            surname = line.split()[4]
            surnames.append(surname)
            date_string = line.strip().split(';')[8]
            date_obj = datetime.strptime(date_string, "%d.%m.%Y")
            year = date_obj.year

            if year in years:
                years[year] += 1
            else:
                years[year] = 1

        duplicate_phones = set([phone for phone in phones if phones.count(phone) > 1])
        num_duplicate_phones = len(duplicate_phones)
        table_num = PrettyTable()
        table_num.field_names = ["Количество повторяющихся номеров телефона", "Повторяющиися номера"]
        table_num.add_row([num_duplicate_phones, duplicate_phones])
        print(table_num)

        surname_counts = Counter(surnames)
        duplicate_surnames = [surname for surname, count in surname_counts.items() if count > 1]
        num_duplicate_surnames = len(duplicate_surnames)
        samesurname_count=0
        for surname, count in surname_counts.items():
            if count > 1:
                samesurname_count+=count
        print(samesurname_count)
        table_sur = PrettyTable()
        table_sur.field_names = ["Количество однофамильцев"]
        table_sur.add_row([samesurname_count])
        print(table_sur)

        print("Статистика по годам рождения:")
        table = PrettyTable()
        table.field_names = ["Год", "Количество"]
        for year, count in sorted(years.items()):
            count = years[year]
            table.add_row([year, count])
        print(table)


def read():
    filepath = './test_prog1.csv'
    encoding = d_encoding(filepath)
    with open(filepath, 'r', encoding=encoding) as f:
        reader = csv.reader(f, delimiter=';')
        for i,line in enumerate(reader):
            if right(line[0]) == False:
                wrong_string=f'{i};ИО : {line[3]};Телефон : {line[0]};\n'
                print(wrong_string)
            if right(line[0]) and line[7] == 'pos':
                right_string = f'ФИО: {line[4]};Телефон : {line[0]};Дата Рождения: {line[8]};Возраст на сегодня:{current_age(line[8])};\n'
                with open("pos_h.csv", "a", encoding=encoding) as f:
                    f.write(right_string)
            if right(line[0]) and line[7] == 'cash':
                right_string = f'ФИО: {line[4]};Телефон:{line[0]};Дата Рождения: {line[8]};Возраст на сегодня:{current_age(line[8])};\n'
                with open("cash_h.csv", "a", encoding=encoding) as f:
                    f.write(right_string)

def delete():
    filepath = './test_prog1.csv'
    os.remove(filepath)


def main():
    download()
    read()
    stats()
    delete()


if __name__ == '__main__':
    main()
