p = range(8, 39)
q = range(23, 58)
amin = 100
for a1 in range(1, 100):
    for a2 in range(a1, 100):
        Flag = True
        A = range(a1, a2)
        for x in range(100):
            if not (((x in A) or (not (x in p))) or (x in q)):
                Flag = False
                break
        if Flag:
            if amin > a2 - a1:
                amin = a2 - a1
print(amin)
