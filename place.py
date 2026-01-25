def f(x, k, v):
    if x <= 17:
        return k in v
    if k >= max(v):
        return 0
    h = [f(x - 1, k + 1, v)]
    if x % 3 == 0:
        h.append(f(x // 3, k + 1, v))
    else:
        h.append(f(x - 2, k + 1, v))
    if x % 5 == 0:
        h.append(f(x // 5, k + 1, v))
    else:
        h.append(f(x - 3, k + 1, v))
    print(h)
    if k % 2 != max(v) % 2:
        return any(h)
    else:
        return all(h)


for x in range(17, 10000):
    if f(x, 0, [2]) == 1:
        print('Задача 19:', x)
        break