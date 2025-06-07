n = int(input())
arr = []
for i in range(0, n):
    a = int(input())
    arr.append(a)
for i in range(0, n):
    flag = True
    for j in range(0, n):
        if arr[j] % arr[i] != 0:
            flag = False
            break
    if flag:
        elem = arr[i]
        arr = [print(x // elem) for x in arr]
        break
if flag == False:
    print("Не поделилось")

