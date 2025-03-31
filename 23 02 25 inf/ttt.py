results = []
for x in "01234567":
    for y in "01234567":
        t = int(y + "04" + x + "5" , 11) + int("253" + x + y, 8)
        if t % 117 == 0:
            results.append(t)
print(results)
print(min(results)//117)
