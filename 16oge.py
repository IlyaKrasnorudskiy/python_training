n = int(input()) # Количество вводимых чисел
count = 0 # здесь хранится количество подходящих под усл. чисел
for i in range(0, n):
    a = int(input())
    if a % 4 == 0 and a % 7 != 0:
        count = count + 1

print(count)