a = 4 ** 36 + 3 * 4 ** 20 + 4**15 + 2 * 4 ** 7 + 49
s = '' #новое число в n СС
base = 16
while a != 0:
    s = str(a % base) + s
    a = a // base
print(set(s))
