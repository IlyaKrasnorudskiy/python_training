f = open("17_a.txt")
arr = []
mins = 9999999
count = 0
maxs = 0
for i in f:
    arr.append(int(i))
for i in range(len(arr)):
    if (arr[i] > 99 and arr[i] < 1000) and arr[i] % 10 == 3:
        mins = min(mins, arr[i])
for i in range(len(arr)-1):
    if ((arr[i] > 999 and arr[i] < 10000) and not(arr[i+1] > 999 and arr[i+1] < 10000)) or ((arr[i+1] > 999 and arr[i+1] < 10000) and not(arr[i] > 999 and arr[i] < 10000)):
        if (arr[i] ** 2 + arr[i+1] ** 2) % mins == 0:
            count += 1
            maxs = max((arr[i] ** 2 + arr[i+1] ** 2), maxs)
print(count, maxs)