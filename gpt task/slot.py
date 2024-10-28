import random
def x(i):
        random.seed(i)
        l = []
        a1 = random.randint(1,10)
        a2 = random.randint(1, 10)
        a3 = random.randint(1, 10)
        a4 = random.randint(1, 10)
        a5 = random.randint(1, 10)
        l.append(a1)
        l.append(a2)
        l.append(a3)
        l.append(a4)
        l.append(a5)
        return l

lis = []
count = 0
for i in range(1, 1000):
    lis.append(x(i))
    if x(i+1) in lis:
        count +=1
print(count)