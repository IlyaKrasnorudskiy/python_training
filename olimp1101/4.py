k = int(input())
arr = []
for i in range(0,k):
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
sums = 0
for i in range(len(arr)):
    if i == len(arr)-1:
        sums += 1
        break
    else:
        sums += arr[i]
print(sums)