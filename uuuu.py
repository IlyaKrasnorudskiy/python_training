a = 729**7 + 3 **16 - 18
s = ""
n = 9
while a!= 0:
    s = str(a % n) + s
    a = a // n
print(s.count("0"))