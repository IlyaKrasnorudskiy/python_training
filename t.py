n = int(input())
A = list(map(int, input().split()))

for i in range(1, n):
    temp = A[i]
    j = i - 1
    while j >= 0 and A[j] > temp:
        print(A)
        A[j + 1] = A[j]
        j -= 1
        print(A)
    A[j + 1] = temp



print(" ".join(map(str, A)))
