for x in "0123456789A":
    for y in "0123456789A":
        v = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
        if v % 305 == 0:
            print(v // 305)