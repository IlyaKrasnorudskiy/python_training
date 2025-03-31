def proverka(x, y):
    y = str(y)
    arr = list(y)
    flag = 1
    for i in str(x):
        if i in arr:
            arr.remove(i)
        else:
            flag = 0
    if flag:
        return True
    else:
        return False
print(proverka(203241, 1213045))