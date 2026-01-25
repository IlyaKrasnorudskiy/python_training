import sys
sys.setrecursionlimit(300000)

def F(n):
    if n <= 10:
        return n
    if n > 10:
        return n - 12 + F(n-21)

print((F(224356)-F(224272))/F(59))
