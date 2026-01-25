from itertools import product

count = 0
for code in product("012345", repeat = 5):
    if (code.count("5") >= 2) and ((code.count("1") + code.count("3")) < 3):
        count += 1

print(count)