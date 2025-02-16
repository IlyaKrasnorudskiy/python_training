
arr = [1,2,54,5,3]

for i in range(len(arr) - 1):
    ind = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[ind]:
            ind = j
    arr[i], arr[ind] = arr[ind], arr[i]

print(arr)