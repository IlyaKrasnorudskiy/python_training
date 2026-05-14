a = int(input())
b = int(input())
c = int(input())
d = int(input())
ab = a * b
cd = c * d
n = 0
na = 0
if ab > cd:
    n = cd
    na = ab
else:
    n = ab
    na = cd
k = n
while k > 2:
    if ab % k == cd % k:
        break
    else:
        k = k - 1
if ab % k == cd % k:
    print(k)
else:
    k = na - n
    print(k)
