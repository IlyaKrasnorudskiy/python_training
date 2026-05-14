# вариант 1: через вложенные списки и формулу номера
rows, cols = 10, 7

a = [[row * cols + col + 1 for col in range(cols)]  # 1..70 по строкам
     for row in range(rows)]

for row in a:
    print(row)
