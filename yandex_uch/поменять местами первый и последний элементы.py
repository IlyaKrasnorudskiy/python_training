n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
maxi = 0
mini = arr[0]
for i in range(0, len(arr)):
    if arr[i] > maxi:
        maxi = arr[i]
        ind = i
arr[0], arr[ind] = arr[ind], arr[0]
print(arr)