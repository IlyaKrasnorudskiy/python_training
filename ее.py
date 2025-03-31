def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n-1)+3*(F(n-2))
    if n > 2 and n % 2 == 0:
        amount = 0
        for i in range(1, n):
            amount += F(i)
            print(i)
        return amount
print(F(28))