s = '9' * 65
while '999' in s or '222' in s:
    if '222' in s:
        s = s.replace('222','9', 1)
    else:
        s = s.replace('999', '2', 1 )

print(s)