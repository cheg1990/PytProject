from DataAnalyze import DataAnalyze
from prettytable import PrettyTable

class FileHandler:
    def __init__(self,data):
        self.data = data

    def format(self, initials, tel, date_of_birth, age):
        analyzer = DataAnalyze(self.data)
        return f'ФИО: {initials};Телефон : {tel};Дата Рождения: {date_of_birth};Возраст на сегодня:{analyzer.calculate_age(age)};\n'

    def write_to_file(self, name_of_file, string_to_write):
        with open(name_of_file, 'a', encoding='utf-8') as f:
            f.write(string_to_write)

    def sort_file(self):
        wrong_numbers = '' # понадобились переменные, чтобы вывести некоректные номера в таблицы, и нужны они за циклом
        count_of_wrong_numbers = 0

        for row in self.data:
            not_fixed_tel_num = row[0]
            analyzer = DataAnalyze(self.data)
            fixed_tel_num = analyzer.clean_phone_number(not_fixed_tel_num)
            name = row[1]
            full_name = row[2]
            type_of_payment = row[3]
            date_of_birth = row[4] # берем с кортежа данные и приравниваем к переменным
            right_string = self.format(full_name, fixed_tel_num, date_of_birth, date_of_birth)

            if len(fixed_tel_num) == 11 and type_of_payment == 'pos':
                self.write_to_file('pos_h.csv', right_string)

            if len(fixed_tel_num) == 11 and type_of_payment == 'cash':
                self.write_to_file('cash_h.csv', right_string)

            if len(fixed_tel_num) == 11 and type_of_payment == 'cards':
                self.write_to_file('cards_h.csv', right_string)

            if len(fixed_tel_num) != 11:
                wrong_numbers += f'{name} {fixed_tel_num}\n'
                count_of_wrong_numbers +=1 # записываем в переменную все некорректные номера и ведем их подсчет

        if count_of_wrong_numbers > 0: # выводим их в таблицу
            table = PrettyTable()
            table.field_names = ['Некоректные номера телефонов']
            table.add_row([wrong_numbers])
            print(table)