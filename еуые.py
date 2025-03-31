def diff_sum_digits(x):
    A = []
    for i in x:
        b = 0
        while i != 0:
            b += i % 10
            i //= 10
        A.append(b)
    for i in range(len(A)):
        b = 0
        for j in range(len(A)):
            if A[i] == A[j]:
                b += 2
        if b > 2:
            return False

    return True

print(diff_sum_digits([1, 2, 3, 4, 101]))
