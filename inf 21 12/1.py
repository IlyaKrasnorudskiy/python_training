rpg = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n % 4 == 0 and n % 10 == 6:
        rpg = rpg + n
print(rpg)