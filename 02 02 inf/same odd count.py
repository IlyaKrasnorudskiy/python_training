A = []
def odd_digit_sum(n):
    global A
    A = []

    for i in n:
        k = 0
        while i != 0:
            digit = i % 10
            if digit % 2 == 1:
                k += 1
            i = i // 10
        A.append(k)
    return A

def same_odd_count(x):
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            return False
            break
    return True


A = odd_digit_sum([2, 4, 6, 8, 81])
print(same_odd_count(A))
