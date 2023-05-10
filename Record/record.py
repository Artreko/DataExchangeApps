from dataclasses import dataclass
from datetime import date


@dataclass
class DataRec:
    name: str
    work_years: int
    birth_date: date

    def __init__(self, name, work_years, birth_date):
        self.name, self.work_years, self.birth_date = name, work_years, birth_date

    def __str__(self):
        return f'{self.name};{self.work_years};{self.birth_date.strftime("%d.%m.%Y")}'


if __name__ == '__main__':
    print(DataRec("Name", 5, date.today().strftime('%d.%m.%Y')))
