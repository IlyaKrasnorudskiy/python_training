for x in "0123456789ABCDE":
    for y in "0123456789ABCDE":
        number1 = int('90'+x+'4'+y, 15)
        number2 = int('91' + x + y + "2", 16)
        if (number1+number2) % 56 == 0:
            print((number1+number2)//56)