# Задача 1


for i in range(2, 10):

    temp_count = 0
    for n in range(2, 100):
        if not n % i:
            temp_count += 1
    print(f'Числу {i} кратны {temp_count} чисел')
