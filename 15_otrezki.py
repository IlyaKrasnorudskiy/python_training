P = [i for i in range(17, 41)]
Q = [i for i in range(20, 58)]
amin = 1002
arr = []
for a1 in range(1, 200):
    for a2 in range(a1+1, 200):
        Flag = 1
        A = [i for i in range(a1, a2)]
        for x in range(-100,100):
            f = (not(x in A)) <= (((x in P) and (x in Q))<=(x in A))
            if not f:
                Flag = 0
                break
        if Flag == 1:
            amin = a2 - a1
            arr.append(amin)
print(min(arr)-1)
