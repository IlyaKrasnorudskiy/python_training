n = int(input())
m = int(input())
a = int(input())
b = int(input())
mins = 9999
minutes = n * 60 + m
if minutes > 22 * 60 or minutes < 8 * 60:
    print("-1")
    exit()
if a < b:
    mins = a
else:
    mins = b
for i in range(0,1000):
    if i * mins >= minutes:
        minutes = abs(minutes - i * mins)
        break
print(minutes)