max_sums = 0
for n in range(4, 2500):
    s = '5'* n + '0'
    while '055' in s or '65' in s or '5555' in s:
        if '055' in s:
            s = s.replace('055','56',1)
        if '65' in s:
            s = s.replace('65','5',1)
        if '5555' in s:
            s = s.replace('5555','000',1)
        if '00000' in s:
            s = s.replace('00000','6',1)
    sums = sum(map(int, s))
    if sums > max_sums:
        max_sums = sums
print(max_sums)