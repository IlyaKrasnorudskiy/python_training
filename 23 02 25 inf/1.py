n = list(map(int, input().split()))
mini = n[0]
for i in range(4):
    if mini > n[i]:
        mini = n [i]
print(mini)