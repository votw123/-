# Задача 5


import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_num = 0
max_num_idx = 0

for idx, item in enumerate(array):
    if (0 > item > max_num) or (max_num == 0 and item < 0):
        max_num, max_num_idx = item, idx

print(array)
print(f'Максимальное отрицательное число: {max_num}; индекс: {max_num_idx}.')
