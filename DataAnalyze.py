from datetime import datetime
from collections import Counter

class DataAnalyze:
    def __init__(self,data):
        self.data = data
        self.fixed_tel_num = [line[0] for line in self.data]
        self.initials = [line[1] for line in self.data]
        self.fullname = [line[2] for line in self.data]
        self.type_of_payment = [line[3] for line in self.data]
        self.dob = [line[4] for line in self.data]

    def calculate_age(self, dob_str):
        dob = datetime.strptime(dob_str, '%d.%m.%Y')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def get_duplicate_phone_numbers(self):
        phones = []
        for line in self.fixed_tel_num:
            phones.append(line)

        duplicate_phones = set([phone for phone in phones if phones.count(phone) > 1])
        return duplicate_phones

    def get_same_surname_count(self):
        surnames = []
        for line in self.fullname:
            surname = line.split()[0]
            surnames.append(surname)

        surname_counts = Counter(surnames)
        samesurname_count = 0

        for surname, count in surname_counts.items():
            if count > 1:
                samesurname_count += count
        return samesurname_count


    def get_age_stats(self):
        years = {}
        for line in self.dob:
            date_obj = datetime.strptime(line, '%d.%m.%Y')
            year = date_obj.year

            if year in years:
                years[year] += 1
            else:
                years[year] = 1
        return years
