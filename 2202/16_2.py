import sys
sys.setrecursionlimit(10000)
def f(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + f(n-1)
print(f(2021) - f(2019))