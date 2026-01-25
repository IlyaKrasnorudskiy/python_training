from itertools import permutations
count = 0
n = 0
alf = 'МУЖЧИНА'
for i in permutations(alf, 6):
    if i[0] != 'Ч' and i.count('Ж') >= 1 :
        n += 1
        if n % 2 != 0:
            count += 1
print(count)