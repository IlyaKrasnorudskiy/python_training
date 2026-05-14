s = 69 * '8'
while "3333" in s or '8888' in s:
    if '3333' in s:
        s = s.replace('3333', '88', 1)
    else:
        s = s.replace('8888', '33', 1)
print(s)