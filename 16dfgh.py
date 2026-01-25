n = int(input())
if n > 1000:
    exit()
maxs = 0
for i in range(0,n):
    a = int(input())
    if a > 30000:
        exit()
    if a % 4 == 0:
        maxs = max(maxs, a)
print(maxs)