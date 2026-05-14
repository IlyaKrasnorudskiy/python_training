def f(n):
    if n < 15:
        return n
    if n >= 15:
        return f(n % 15) * f(n // 15)

count = 0
for n in range(0, 100000000):
    if f(n) == 7560:
        count += 1
print(count)