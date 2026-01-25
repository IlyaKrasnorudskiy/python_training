count = 0 # счетчик
n = int(input()) # кол-во чисел
for i in range(0, n):
    a = int(input("Введите число: "))
    if a % 2 == 0:
        count += 1
print(count)