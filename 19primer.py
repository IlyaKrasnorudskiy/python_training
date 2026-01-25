def F(x, p):
    if x >= 38 and p == 4: return True
    if x < 38 and p == 4: return False
    if x >= 38: return False
    if p % 2 == 0:
        return F(x + 1, p + 1) and F(x + 2, p + 1) and F(x * 2, p + 1)
    else:
        return F(x + 1, p + 1) or F(x + 2, p + 1) or F(x * 2, p + 1)

for s in range(1, 38):
    if F(s, 1):
        print(s)