import sys
sys.setrecursionlimit(10000)
def f(n):
    if n % 2 == 0:
        return 3 + f(n/2)
    if n % 2 != 0 and n % 3 == 0:
        return 2 + f(n/3)
    if n % 2 == 0 and n % 3 != 0:
        return 0

for n in range(0,1000):
    if f(n) == 70:
        print(n)
        break