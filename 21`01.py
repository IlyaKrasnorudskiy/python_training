from itertools import product
for i in range(520,0, -1):
    for code in product("2", repeat = i):
        temp = code
        code = '0' + ''.join(code) + '0'

        while '00' not in code:
            code = code.replace('033', '1302', 1)
            code = code.replace('03', '120', 1)
            code = code.replace('023', '203', 1)
            code = code.replace('02', '20', 1)


        if code.count('1') == 340 and code.count('2') == 849 and code.count('3') == 151:
            print(temp.count("2"))
            print(temp, " - начальная с трока, ] ", code, ' - конечная строка')