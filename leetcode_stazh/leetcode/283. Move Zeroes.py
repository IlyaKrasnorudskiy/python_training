def MoveZeros(a):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            a.append(a.pop(i))
    return a
print(MoveZeros([0,0,1]))