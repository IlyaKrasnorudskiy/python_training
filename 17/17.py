f = open("17 (7).txt")
count = 0
maxs = 0

arr = [int(i) for i in f]
mins = 999999
for i in arr:
    a = str(i)
    if a[-1] == a[-2]:
        if int(a) < mins:
            mins = int(a)
for i in range(0, len(arr)-1):
    if (arr[i] % 7 == 0 and arr[i+1] % 7 != 0) or (arr[i] % 7 != 0 and arr[i+1] % 7 == 0):
        s1 = str(arr[i])
        s2 = str(arr[i+1])
        if (s1[-1] == s2[-2]) or (s2[-1] == s1[-2]):
            if arr[i] ** 2 + arr[i+1] ** 2 <= mins**2:
                count += 1
                maxs = max(maxs, arr[i] ** 2 + arr[i+1] ** 2)

print(count, maxs)
