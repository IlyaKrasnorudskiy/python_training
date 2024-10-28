for a in range(1,1000):
    flag = 1
    for x in range(1,1000):
        if ((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))) == 1:
            pass
        else:
            flag = 0
    if flag == 1:
        print(a)