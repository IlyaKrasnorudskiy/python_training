from itertools import product

N = int(input())

count = 0
for i in range(1, 30):
    for code in product("25", repeat = i):
        count += 1
        result = ''.join(code)
        if result == str(N):
            print(count)
            break