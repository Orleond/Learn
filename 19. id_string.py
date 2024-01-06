id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'
id_list = id_string.split(' ')
id_set = set()
for i in range(len(id_list)):
    length = len(id_set)
    id_set.add(id_list[i])
    if length == len(id_set):
        print(f'Найден дубликат id {id_list[i]}')
