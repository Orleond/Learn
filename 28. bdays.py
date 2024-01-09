import datetime as dtime

FORMAT = '%d.%m.%Y'
lera = dtime.date(2015, 5, 16)
maxim = dtime.date(2011, 12, 16)

birthdays = [
    ('Лера', '16.05.2015'),
    ('Максим', '16.12.2011'),
    ('Сергей', '21.10.1991')
]


def get_days_to_birthday(name, date_birthday):
    today = dtime.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)
    if date_birthday < today:
        date_birthday = date_birthday.replace(year=today_year + 1)
    return f'{name}, до твоего дня рождения осталось дней: {date_birthday - today}'


for values in birthdays:
    print(get_days_to_birthday(values[0], dtime.datetime.strptime(values[1], FORMAT).date()))