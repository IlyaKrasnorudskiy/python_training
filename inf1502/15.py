def treyg(n,m,k):
    if n + m > k and n + k > m and m + k > n:
        return True
    else:
        return False
for A in range(300, 0, -1):
    k = 0
    for x in range(400):
        if ((treyg(x,10, 20) <= (not(max(x,8) > 24))) == (not treyg(3,A,x))):
            k += 1
    if k == 400:
        print(A)
        break