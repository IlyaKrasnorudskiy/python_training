import math
n = int(input())
mas = []
for i in range(n):
    a = int(input())
    if abs(a) >= 30 and abs(a) <= 300:
        mas.append(a)
count_mens = 0
count_women = 0
sums_mens = 0
sums_women = 0
for i in range(0, len(mas)):
    if mas[i] > 0:
        sums_mens += abs(mas[i])
        count_mens += 1
    else:
        sums_women += abs(mas[i])
        count_women += 1
print(math.floor(sums_mens / count_mens), math.floor(sums_women / count_women))
