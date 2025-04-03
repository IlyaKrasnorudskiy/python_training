count = 0
for x1 in range(0,2):
    for x2 in range(0, 2):
        for x3 in range(0, 2):
            for x4 in range(0, 2):
                if (((x1 > x2)) <= x3) == 1 and (((x2 > x3)) <= x4) == 1:
                    count += 1
                    print(x1,x2,x3,x4)
print(count)