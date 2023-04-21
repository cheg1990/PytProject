from DataAnalyze import DataAnalyze

class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def format(self,initials, tel, date_of_birth, age, data):  # функция для формата записи в файл
        analyzer = DataAnalyze(data)
        return f'ФИО: {initials};Телефон : {tel};Дата Рождения: {date_of_birth};Возраст на сегодня:{analyzer.calculate_age(age)};\n'

    def write_to_file(self, name_of_file, string_to_write):
        with open(name_of_file, 'a', encoding='utf-8') as f:
            f.write(string_to_write)

    def sort_file(self, data):
        lines = '\n'.join(data)
        for i, line in enumerate(lines.split('\n')):
            cells = line.split(';')
            if len(cells) < 9:
                continue
            not_fixed_tel_num = cells[0]
            analyzer = DataAnalyze(data)
            fixed_tel_num=analyzer.clean_phone_number(not_fixed_tel_num)
            name = cells[3]
            full_name = cells[4]
            date_of_birth = cells[8]
            type_of_payment = cells[7]
            right_string = self.format(full_name,fixed_tel_num, date_of_birth, date_of_birth, data)
            if len(fixed_tel_num) != 11:
                wrong_string = f'{i};ИО : {name};Телефон : {fixed_tel_num};\n'
                print(wrong_string)
            if len(fixed_tel_num)==11 and type_of_payment == 'pos':
                self.write_to_file('pos_h.csv', right_string)
            if len(fixed_tel_num)==11 and type_of_payment == 'cash':
                self.write_to_file('cash_h.csv', right_string)

