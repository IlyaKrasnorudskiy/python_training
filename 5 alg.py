l = []
for n in range(0, 1000):
    r = bin(n)[2::]
    if n % 3 == 0:
        r = r + r[-3::]
    if n % 3 != 0:
        r = r + bin((n % 3) * 3)[2::]
    if int(r, 2) > 151 :
        l.append(int(r, 2))
print(min(l))