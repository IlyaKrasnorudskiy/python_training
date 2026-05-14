for x in "0123456789ABCDEFGHI"[::-1]:
    a = int("CD" + x + "34", 19)
    b = int('7' + 'F' + x + '2E', 19)

    if (a+b) % 18 == 0: 
        print((a+b) // 9)