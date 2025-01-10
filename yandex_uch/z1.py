s = input().strip()

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end=' ')
    else:
        print(s[i], end='')
    print()
