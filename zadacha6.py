k = int(input())
l = int(input())
n = int(input())
s = int(input())
if s % 2!= 0:
    exit()
points_stef = k+n*s
points_opp = l+n*s/2

if points_stef < points_opp:
    print("NO")
else:
    for i in range(1, n+1):
        k += s
        l += s/2
        if k >= l:
            print("Yes")
            print(i)
            break
