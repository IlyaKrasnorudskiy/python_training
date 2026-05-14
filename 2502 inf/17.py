def calc(n):
    if n > 99 and n < 1000:
        return 1
    else:
        return 0

f = open("17_2024.txt")
s = [int(i) for i in f]
count = 0
maxs = -1
sums = 0
for j in s:
    if j % 100 == 13 and maxs < j:
        maxs = j
for i in range(0,len(s)-2):
    if (calc(s[i])!= 1 and calc(s[i+1])== 1 and calc(s[i+2]) == 1) or (calc(s[i])== 1 and calc(s[i+1])!= 1 and calc(s[i+2]) == 1) or (calc(s[i])== 1 and calc(s[i+1])== 1 and calc(s[i+2]) != 1):
        if s[i] + s[i+1] + s[i+2] <= maxs:
            count += 1
            if sums < s[i] + s[i+1] + s[i+2]:
                sums = s[i] + s[i+1] + s[i+2]

print(count, sums)