import datetime as dtime

FORMAT = '%H:%M:%S'
storage_data = {}
weight = 75  # Вес
height = 175  # Рост
len_step_m = 0.65  # Длина одного шага в метрах
last_time = dtime.time(0, 0, 0)
distance = 0
calories = 0
hours = 0


def show_message(time, steps, distance, calories, achievements):
    print(f'''Время обращения: {time}.
Количество шагов за сегодня: {steps}.
Дистанция составила: {distance} км.
Вы сожгли {calories} ккал.
{achievements}''')


def check_correct_data(data):
    result = True
    if len(data) != 2:
        result = False
    if data[0] is None or data[1] is None:
        result = False
    return result


def check_correct_time(time):
    time = dtime.datetime.strptime(time, FORMAT)
    time = dtime.time(time.hour, time.minute, time.second)
    if time > last_time:
        return True
    else:
        return False


def get_step_day(steps):
    sum = 0
    for step in steps.values():
        sum += step
    return sum


def get_distance(steps):
    return steps * len_step_m / 1000


def get_spent_calories(distance, current_time):
    current_time = dtime.datetime.strptime(current_time, FORMAT)
    hours = current_time.minute / 60 + current_time.hour
    return (35 * weight + (distance * 1000 / hours / 1000) ** 2 / height * (29 * weight)) / 1000 * hours * 60


def get_achievement(dist):
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


def accept_package(package_data):
    if not check_correct_data(package_data):
        print('Критическая ошибка. Некорректные данные в пакете')
        return
    if not check_correct_time(package_data[0]):
        print('Ошибка в передаваемом времени')
        return
    return storage_data


package_data = ("12:22:22", 2300)
distance = get_distance(package_data[1])
calories = get_spent_calories(distance, package_data[0])
accept_package(package_data)
show_message(package_data[0], package_data[1], distance, calories, get_achievement(distance))