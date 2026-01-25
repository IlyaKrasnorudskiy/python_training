def f(x, z):
    if x > 45: return z%2==0
    if z == 0: return 0
    h = [f(x + x//i, z-1) for i in range(2, x+1) if x % i == 0]
    if (z-1)%2==0:
        return any(h)
    return all(h)
print(19, len([s for s in range(2, 45) if f(s, 2)]))
print(20, [s for s in range(1, 45) if (not f(s, 1)) and f(s, 3)])
print(21, [s for s in range(1, 45) if ((f(s, 2)) or f(s, 4)) and (not f(s, 2))])