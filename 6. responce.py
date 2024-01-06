response = 424562

minute = 60
hour = 60 * 60
day = 60 * 60 * 24

days = response // day
response = response - days * day
hours = response // hour
response = response - hours * hour
minutes = response // minute
response = response - minutes * minute
seconds = response

print(days, 'дней', hours, 'часов', minutes, 'минут', seconds, 'секунд.')
