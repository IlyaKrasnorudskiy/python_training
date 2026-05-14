def f(n):
    if n < 10:
        return n
    if n >= 10:
        return f(n % 10) + f(n // 10)

count = 0
for n in range(2**63, 0, -1):
    if f(n) == 159:
        count += 1
print(count)