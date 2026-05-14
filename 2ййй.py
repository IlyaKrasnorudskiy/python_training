for p in range(15, 45):
    b = int('1011' + '967'+ '13'+ '8', p) + int('14'+ '435'+ '10'+ '98', p)
    if b % (p-1) == 0:
        print(p)
