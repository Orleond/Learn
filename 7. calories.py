weight = 75   # Вес
height = 175  # Рост
dist = 9.75   # Расстояние в км
hours = 2     # Время движения в часах
minutes = hours * 60

calories = (35 * weight + (dist * 100 / hours / 100) ** 2 / height * (29 * weight))/1000 * minutes
print(calories)
