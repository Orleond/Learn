def get_mean(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum / len(num_list)
num_list = [3, 6, 5, 7, 9, 1]
print(f'{get_mean(num_list):.2f}')