arr = []
k = 1
for i in range(2, 900001):
    diap = int(i**0.5)
    a = []
    for j in range(2, i+1):
        if i % j == 0:
            a.append(j)
            if i // j != j:
                a.append(i//j)
    if len(a) >= 2:
        kv = min(a) ** 2 + max(a)
        flag = 1
        d1 = int(kv**0.5)
        for l in range(2, d1):
            if kv % l == 0:
                flag = 0
                break
        if flag == 1:
            arr.append(str(i) + str(kv))
            k += 1
    if k > 5 :
        break
for x in range(len(arr)-1, -1,-1):
    print(arr[j])
