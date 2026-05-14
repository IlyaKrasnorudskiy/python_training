for n in range(1,100000):
    dec = n
    b  = bin(n)[2:]
    for i in range(0,3):
        sums = sum(map(int, str(dec)))
        if sums % 2 == 0:
            b  += '0'
            dec = int(b,2)
        else:
            b  += '1'
            dec = int(b,2)
    if dec > 2054:
        print(dec)