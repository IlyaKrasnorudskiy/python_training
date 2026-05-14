m = 10**6
P = [i for i in range(17, 35)]
Q = [i for i in range(37, 84)]
for Amin in range(1, 200):
    for Amax in range(Amin + 1, 200):
        check = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(-300, 300):
            f = (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))
            if not f:
                check = 0
                break
        if check == 1:
            m = min(m,Amax - Amin)
print(m-1)