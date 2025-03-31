count = 0
for i in range(1111, 777778):
    if i % 9 == 0 and i % 7 != 0 and i % 17 != 0 and i % 37 != 0 and i % 47 != 0:
        count += 1
print(count)