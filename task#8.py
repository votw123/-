# Задача 8

NUM_COLUMNS = 4
NUM_ROWS = 5

result = list()
for row in range(NUM_ROWS):
    row_sum = 0
    result.append(list())
    for col in range(NUM_COLUMNS - 1):
        result[row].append(input('Введите {} число {} строки '.format(col + 1, row + 1)))
        row_sum += float(result[row][col])
    result[row].append(str(row_sum))

for row in result:
    print('\t'.join(row))