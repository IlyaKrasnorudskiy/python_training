f = open("24_2.txt").readline()
max_len = 0
for i in range(0, len(f)):
    x_count = 0
    y_count = 0
    current_len = 0
    for j in range(i, len(f)):
        if f[j] == "X":
            x_count += 1
        elif f[j] == "Y":
            y_count += 1

        current_len += 1
        if x_count == 1 and y_count == 1:
            max_len = max(max_len, current_len)
        elif x_count > 1 or y_count > 1:
            break
print(max_len)