count = 0
for x in range(77778, 99999+1):
    x = str(x)
    if x[0] < x[1] and x[1] < x[2] and x[2] > x[3] and x[3] > x[4]:
        count += 1
        print(x)
print(count)