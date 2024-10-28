count = 0
i = 460000001
while count < 5:
    cdel = 0
    half_i = i // 2
    for j in range(2, half_i + 1):
        if i % j == 0:
            cdel += 1
            if cdel == 5:
                print(i // j)
                count += 1
                break
    i += 1