n = int(input())
arr = []
for i in range(0, n):
    a = int(input())
    arr.append(a)
maks = arr[0]
count = 0
for i in range(n):
    if maks < arr[i]:
        maks = arr[i]

for i in range(n):
    if arr[i] != maks:
        count = count + (maks - arr[i])

print(count)