from prettytable import PrettyTable

class DataView:
    def __init__(self, data_analyze):
        self.data_analyze = data_analyze

    def show_duplicate_phone_numbers(self):
        duplicate_phones = self.data_analyze.get_duplicate_phone_numbers()
        num_duplicate_phones = len(duplicate_phones)
        table = PrettyTable()
        table.field_names = ['Количество повторяющихся номеров телефона', 'Повторяющиеся номера']
        table.add_row([num_duplicate_phones, duplicate_phones])
        print(table)

    def show_same_surname_count(self):
        samesurname_count = self.data_analyze.get_same_surname_count()
        table = PrettyTable()
        table.field_names = ['Количество однофамильцев']
        table.add_row([samesurname_count])
        print(table)

    def show_age_stats(self):
        age_stats = self.data_analyze.get_age_stats()
        table = PrettyTable()
        table.field_names = ['Год', 'Количество записей']

        for year, count in sorted(age_stats.items()):
            table.add_row([year, count])
        print(table)
