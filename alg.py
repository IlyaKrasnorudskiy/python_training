import random
for i in range(0,1000):
    print(*random.choices((1, 6, 8, 9), k=3))