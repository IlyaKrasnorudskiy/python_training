def same_length(x):
    if not x:
        return True
    fl = len(x[0])
    for i in x:
        if len(i) != fl:
            return False
    return True

