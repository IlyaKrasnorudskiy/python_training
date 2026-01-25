n = int(input())
text = str(input())
text = text.split()
count = 0
for i in range(0, n):
    if 1 <= int(text[i]) <= 109:
        count += bin(int(text[i]))[2::].count("1")
    else:
        exit()
print(count)