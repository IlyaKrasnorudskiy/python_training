f = open("17.txt")
arr = []
mins = 1000
count = 0
m = 0
for i in f:
    arr.append(int(i))
for i in range(0, len(arr)-1):
    if arr[i] % 10 == 5:
        mins = min(mins, arr[i])
for i in range(0, len(arr) - 1):
    if ((arr[i] < arr[i+1] and (arr[i] % 10 == 5)) or (arr[i] > arr[i+1] and (arr[i+1] % 10 == 5))) and ((arr[i] ** 2 + arr[i+1]**2) < mins ** 2):
        m = max(m, arr[i] ** 2 + arr[i+1]**2)
        count += 1

print(count, m)