from DataAnalyze import DataAnalyze
from prettytable import PrettyTable

class FileHandler(DataAnalyze):

    def write_to_file(self, name_of_file, string_to_write):
        with open(name_of_file, 'a', encoding='utf-8') as f:
            f.write(string_to_write)


    def sort_file(self):
        wrong_numbers = ''
        count_of_wrong_numbers = 0

        for index, line in enumerate(self.data):
            fixed_tel_num = self.fixed_tel_num[index]
            type_of_payment = self.type_of_payment[index]
            dob = self.dob[index]
            full_name = self.initials[index]
            phone_len = len(fixed_tel_num)
            right_string = f'ФИО: {full_name}; Телефон: {fixed_tel_num}; Дата Рождения: {dob}; Возраст на сегодня: {super().calculate_age(dob)}\n'

            if phone_len == 11 and type_of_payment == 'pos':
                self.write_to_file('pos_h.csv', right_string)

            elif phone_len == 11 and type_of_payment == 'cash':
                self.write_to_file('cash_h.csv', right_string)

            elif phone_len == 11 and type_of_payment == 'cards':
                self.write_to_file('cards_h.csv', right_string)

            elif phone_len != 11:
                wrong_numbers += f'{full_name} {fixed_tel_num}\n'
                count_of_wrong_numbers += 1

        if count_of_wrong_numbers > 0:
            table = PrettyTable()
            table.field_names = ['Некоректные номера телефонов']
            table.add_row([wrong_numbers])
            print(table)


