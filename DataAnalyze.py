import re
from datetime import datetime
from collections import Counter

class DataAnalyze:
    def __init__(self, data):
        self.data = data

    def clean_phone_number(self, line):
        pattern = r'\D+'
        digits_only = re.sub(pattern, '', line)
        return digits_only

    def calculate_age(self, dob_str):
        dob = datetime.strptime(dob_str, '%d.%m.%Y')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def get_duplicate_phone_numbers(self):
        phones = []
        for line in self.data:
            phone = line[0]
            phones.append(phone)

        duplicate_phones = set([phone for phone in phones if phones.count(phone) > 1])
        return duplicate_phones

    def get_same_surname_count(self):
        surnames = []
        for line in self.data:
            full_name = line[2]
            surname = full_name.split()[0]
            surnames.append(surname)

        surname_counts = Counter(surnames)
        samesurname_count = 0

        for surname, count in surname_counts.items():
            if count > 1:
                samesurname_count += count
        return samesurname_count

    def get_age_stats(self):
        years = {}
        for line in self.data:
            date_string = line[4]
            date_obj = datetime.strptime(date_string, '%d.%m.%Y')
            year = date_obj.year

            if year in years:
                years[year] += 1
            else:
                years[year] = 1
        return years