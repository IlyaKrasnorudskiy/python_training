a = 25
s = ''
while a != 0:
    s = str(a % 2) + s
    a = a//2
print(s)