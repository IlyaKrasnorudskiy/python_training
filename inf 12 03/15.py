count = 0
for A in range(300):
    k = 0
    for x in range(400):
        for y in range(400):
            if ((x< A) <= (x*x < 100)) and ((y * y <= 64) <= (y <=A)):
                k += 1
    if k == 160000:
        count+=1
print(count)

