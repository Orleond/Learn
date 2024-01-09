import datetime as dtime

lera = dtime.date(2015, 5, 16)
maxim = dtime.date(2011, 12, 16)

today = dtime.date.today()
today_year = today.year

lera = lera.replace(year = today_year)
maxim = maxim.replace(year = today_year)
lera_days_left = lera - today
maxim_days_left = maxim - today

print(lera_days_left)
print(maxim_days_left)
