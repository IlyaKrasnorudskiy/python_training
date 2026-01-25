from itertools import product
def alg(l):
    A = "0" + l + "0"
    while "00" not in A:
        if "011" in A:
            A = A.replace("011", "101", 1)
        else:
            A = A.replace("01", "40", 1)
            A = A.replace("02", "20", 1)
            A = A.replace("0222", "1401", 1)
    if A.count("1") == 6 and  A.count("2") == 9:
        return A.count("4")
    else:
        return 0


for i in range(2, 500, 2):
    for code in product("12", repeat = i):
        if code.count("1") == code.count("2"):
            l = "".join(code)
            print(alg(l))