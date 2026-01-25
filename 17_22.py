f = open("17.txt")
maxs = 0
count = 0
arr =[int(i) for i in f]
for i in range(0, len(arr) - 1):
    for j in range(i+1, len(arr)):
        if (arr[i] + arr[j]) % 2 != 0 and (arr[i] * arr[j]) % 3 == 0:
            count += 1
            maxs = max(maxs, arr[i] + arr[j])

print(count, maxs)