count = 0
for n in range (38190000,49000000):
    s = bin(n)[2:]
    if n % 3 <= 1:
        s = s + '0' + bin(n%3)[2:]
    else:
        s = s + bin(n%3)[2:]
    r = int(s,2)
    if r%5 <= 1:
        s = s + '00' + bin(r % 5)[2:]
    elif r % 5 <= 3:
        s = s + '0' + bin(r % 5)[2:]
    else:
        s = s + bin(r % 5)[2:]
    r = int(s, 2)
    if r >= 1222222222 and r <= 1555555666:
        count += 1
print(count)