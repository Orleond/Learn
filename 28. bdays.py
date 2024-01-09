import datetime as dtime

lera = dtime.date(2015, 5, 16)
maxim = dtime.date(2011, 12, 16)

def get_days_to_birthday(date_birthday):
    today = dtime.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year = today_year)
    if date_birthday < today:
        date_birthday = date_birthday.replace(year = today_year + 1)
    return date_birthday - today

print(get_days_to_birthday(lera))
print(get_days_to_birthday(maxim))
