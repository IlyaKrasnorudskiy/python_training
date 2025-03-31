alf = 36
slovo = ''
count = 0
for a1 in range(1,alf):
    for a2 in range(1,alf):
        for a3 in range(1,alf):
            slovo = a1 + a2 + a3
            if a1 + a2 + a3 == 36 and a1 > 0 and a2 > 0 and a3 > 0:
                count += 1

print(count)