for n in range(10000, 1, -1):
    r = bin(n)[2::]
    if n % 3 == 0:
        r += r[-3::]
    if n % 3 != 0:
        r += bin((n % 3) * 3)[2::]
    if int(r, 2) < 100:
        print(n)
        break
