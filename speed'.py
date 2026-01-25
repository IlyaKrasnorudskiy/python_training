s = 0.0
b = False
n = int(input())
for i in range(n):
    a = int(input())
    s = s + a
    if a >= 60:
        b = True
print(round(s / n, 2))
if b:
    print('YES')
else:
    print('NO')