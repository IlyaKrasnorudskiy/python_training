from itertools import product
for i in range(0,23):
    for code in product("12", repeat = i):
        temp = code
        code = ''.join(code)
        if code.count('1') == 10 and code.count('2') > 0:
            while '12' in code:
                code = code.replace('12', '4', 1)

            result = code.count('1') * 1 + code.count('2') * 2 + code.count('4') * 4

            if result == 25:
                print(temp.count("2"))
                print(temp, " - начальная строка, ] ", code, ' - конечная строка')