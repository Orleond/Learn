def test_range(start, end, *nums):
    numbers_list = []
    for i in nums:
        if i in range(start, end+1):
            numbers_list.append(i)
        else:
            print('Число за границами диапазона')
    return numbers_list

print(test_range(4, 12, 5, 16, 32, 6, 7, 1))