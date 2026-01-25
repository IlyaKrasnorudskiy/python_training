def name(n):
    numbers = []
    n = str(n)
    numbers.append(n[0])
    for i in range(1, len(n)):
        if n[i] not in numbers:
            numbers += n[i]
        else:
            return 0
    return 1

count = 0
for n in range(0, 10**11, 5):
    if name(n):
        count += 1
print(count)