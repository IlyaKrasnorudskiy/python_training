s = "Hello, world!"
slovar = {}
maxsumcount = 0
for i in s:
    if i not in slovar:
        slovar[i] = 0
    slovar[i] += 1
    maxsumcount = max(maxsumcount, slovar[i])
sorteduniqsum = sorted(slovar.keys())
for row in range(maxsumcount, 0, -1):
    for i in sorteduniqsum:
        if slovar[i] >= row:
            print("#", end = '')
        else:`
            print(' ', end = '')
    print()
print(''.join(sorteduniqsum))


