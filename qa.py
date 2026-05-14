m = 1000
P = [i for i in range(22, 73)]
Q = [i for i in range(42, 103)]
for Amin in range(1, 20):
    for Amax in range(Amin + 1, 20):
        check = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(-100, 100):
            f = (not((x in A) and (x in P)) or (x in Q))
            if not f:
                check = 0
                break
        if check == 1:
            m = min(m,Amax - Amin)
print(m-1)