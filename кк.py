def F(a, b):
    if b == 0:
        return 0
    if a > b:
        return F(a-1,b)+b
    if a <= b and b > 0:
        return F(a, b-1)+a
count = 0
for a in range(1, 2097153):
        if 2097152 % a == 0:
            count += 1
print(count)