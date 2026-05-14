mas = [i for i in range(1, 300)]
cols = 6

# транспонируем в столбцы
matrix = [mas[i::cols] for i in range(cols)]

# выводим построчно (строки матрицы = столбцы исходного списка)
for row in matrix:
    print(' '.join(f"{x:3d}" for x in row))
