import sys
sys.setrecursionlimit(10000)
def f(n):
    return 2*(g(n-3)+8)

def g(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return g(n-2)+1
print(f(15548))