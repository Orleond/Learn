days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]
tuple_list = []
i = 0
while i < len(days):
    element = days[i], steps[i]
    tuple_list.append(element)
    i += 1
print(tuple_list)
