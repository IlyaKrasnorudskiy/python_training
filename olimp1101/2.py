n = int(input())
count = 0
temp = n
for i in range(2, 16):
    s = ""
    n = temp
    while n != 0:
        s = str(n % i) + s
        n = n // i
    if s[-1] == "0" and s[-2] == "0":
        count += 1
print(count)