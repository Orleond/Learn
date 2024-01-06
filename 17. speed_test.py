import time
num_set = set()
for num in range(10**6):
    num_set.add(num)

start_time = time.time()
if 954365 in num_set:
    print(True)
print((time.time() - start_time))

num_list = []
for num in range(10**6):
    num_list.append(num)

start_time = time.time()
if 954365 in num_list:
    print(True)
print((time.time() - start_time))
