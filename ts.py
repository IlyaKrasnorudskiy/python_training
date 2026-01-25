from itertools import product

for i in range(2, 500, 2):
    for code in product("10", repeat = 6):
        print(code)