s = [3,45,12,124,5,-3,2,-54,53,0]
x = int(input())
c = 0
for i in range(len(s)):
    if s[i] == x:
        print(i)
        c+=1
        break
if not c:
    print("-1")

