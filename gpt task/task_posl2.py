n = int(input("Введите количество чисел: "))
mas = []
for i in range(0, n):
    a = int(input("Введите число: "))
    mas.append(a)
count = 0
for i in range(1, len(mas)):
    if mas[i] == mas[i-1]:
        print(mas[i], mas[i-1])
        count += 1

print(count)