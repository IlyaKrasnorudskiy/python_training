def f (n):
    if n < 3:
        return 1
    if n > 2:
        sums = 0
        for i in range(1, n):
            sums += f(i)
        return sums
print(f(18))