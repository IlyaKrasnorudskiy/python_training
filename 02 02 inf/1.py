a = 12345
sums = 0
while a != 0 :
    sums = sums + a % 10
    a = a//10
print(sums)