n = int(input())
p = []

for i in range(n):
    id, score = map(int, input().split())
    p.append((id, score))
print(p)

p.sort(key=lambda x: (-x[1], x[0]))
for p in p:
    print(p[0], p[1])
