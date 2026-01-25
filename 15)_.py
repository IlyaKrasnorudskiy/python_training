count = 0
for n in range(240000000, 10000000000):
    a = bin(n)[2:]
    a = a + bin(n%4)[2:]
    a = int(a, 2)
    if a >= 1000000000 and a <= 1789456123:
        count += 1
print(count)