from itertools import product
cnt = 0

for code in product("0123456789abcde", repeat = 4):
    if code[0] != 0:
        if code.count("8") == 1:
            if code[0] != code[1] and code[1] != code[2] and code[2] != code[3]:
                cnt += 1
print(cnt)