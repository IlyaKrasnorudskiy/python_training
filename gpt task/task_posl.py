mas = [10, -4, 12, 56, -4, 0]
count = 0
for i in range (0, len(mas)-1):
    if mas[i] == 0:
        break
    if (mas[i-1] * mas[i]) < 0:
        count += 1


print(count)