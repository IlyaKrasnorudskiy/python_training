days = []
n = int (input())
for i in range(1, n+1):
    day = int(input())
    days.append(day)
l = 0
max_l = 0
for d in days:
    if d > 0:
        l+=1
        max_l = max(l, max_l)
    else:
        l = 0
print(max_l)