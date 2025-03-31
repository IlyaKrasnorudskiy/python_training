n = int(input())
num = 0
while n > 0:
    one = n % 10
    if one > 5:
        num += one
    n //= 10
print(num)
print()