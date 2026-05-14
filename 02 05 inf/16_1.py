count = 0
flag = 0
n = int(input())
for i in range(0,n):
    a = int(input())
    if a < 5:
        count += 1
    if a == 10:
        flag = 1
print(count)
if flag == 1:
    print("YES")
else:
    print("NO")