weight = 75        # Вес
height = 175       # Рост
steps = 8462       # Количество пройденных за день шагов
hours = 2          # Время движения в часах
len_step_m = 0.65  # Длина одного шага в метрах
transfer_coeff = 1000  # Коэффициент перевода значения расстояния из метров в километры
minutes = hours * 60

dist = steps * len_step_m / transfer_coeff

calories = (35 * weight + (dist * 1000 / hours / 1000) ** 2 / height * (29 * weight))/1000 * minutes
if dist >= 6.5:
    congrats = 'Отличный результат! Цель достигнута.'
elif dist >= 3.9:
    congrats = 'Неплохо! День был продуктивным'
elif dist >= 2:
    congrats = 'Маловато, но завтра наверстаем!'
else:
    congrats = 'Лежать тоже полезно. Главное - участие, а не победа!'
    
output = f'''Сегодня вы прошли {steps} шагов.
Пройденная дистанция {dist:.2f} км.
Вы сожгли {calories:.2f} ккал.
{congrats}'''
print(output)
