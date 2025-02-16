n = 10000
a = []
c = []
while n > 0:
    b = n % 10
    c.append(b)
    a.append(b)
    n = (n - b) // 10
print(a)
print(c)
for i in range(0, len(a)):
    if a[i]==0:
        c.remove(0)
    else:
        break
print(c)