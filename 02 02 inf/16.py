def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return F(n-2)+F(n-1)
print(F(9))