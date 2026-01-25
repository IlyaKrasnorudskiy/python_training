from itertools import product
count = 0
k1 = 0 # кол-во нечетных
k2 = 0 # кол-во четных
for code in product("НЧ", repeat = 11):
    code = "".join(code)
    if code.count("Н") == 3:
        if code.count("НН") == 0:
            if code[0] == "Н":
                k1 += 1
            else:
                k2 += 1
print(k1 * 4 ** 11 + k2 * 3 * 4**10)
