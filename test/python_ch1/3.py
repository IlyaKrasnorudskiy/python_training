count_zakl = 0
count_volsh = 0
while True:
    a = str(input())
    if int(a) == 0:
        break
    if int(a) > 0:
        srez = int(a[len(a)-2:])
        if srez == 55:
            count_zakl += 1
        if srez > 60 and srez < 80:
            count_volsh += 1
print(count_zakl)
print(count_volsh)