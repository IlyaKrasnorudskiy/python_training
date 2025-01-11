s = [3,45,12,124,5,-3,2,-54,53,0]
l = []
temp = max(s[0], s[1])
max_num = min(s[0], s[1])
for i in range(len(s)):
    if s[i] > max_num:
        temp = max_num
        max_num = s[i]
    elif s[i] > temp:
        temp = s[i]


print(max_num, temp)