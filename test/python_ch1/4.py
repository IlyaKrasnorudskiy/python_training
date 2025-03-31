n = int(input())
if n < 0:
    exit()
n = str(n)
mins = 9
for i in range(0, len(n)):
    if int(n[i]) < mins:
        mins = int(n[i])
for i in range(0, len(n)):
    if int(n[i]) == mins:
        n = n.replace(n[i],'9')
print(n)