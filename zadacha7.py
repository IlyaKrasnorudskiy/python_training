n = int(input())
x = int(input())
attacks = []

for i in range(1, n + 1):
    if (i - x) not in attacks:
        attacks.append(i)

print(attacks)
