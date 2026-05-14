table_data = [
    [46, 13, 32, 36, 31, 25, 24, 38, 20, 29],
    [3, 45, 17, 30, 31, 40, 10, 5, 39, 34],
    [30, 36, 11, 6, 42, 37, 45, 29, 45, 15],
    [8, 23, 16, 4, 33, 18, 24, 37, 28, 36],
    [48, 12, 49, 4, 27, 38, 35, 6, 20],
    [25, 43, 14, 27, 30, 41, 49, 48, 17],
    [40, 17, 47, 1, 12, 38, 32, 17]
]
count = 0
condition = table_data[0][0]
j = -1
for condition in range(0, len(table_data)):
    cond_pos = condition
    temp_condition = table_data[condition][j+1]
    j += 1
    while True:
        try:
            if temp_condition % 4 == 0:
                temp_condition += table_data[cond_pos][j+1]
                j += 1
            elif temp_condition % 4 == 1:
                temp_condition += table_data[cond_pos][j-1]
                j -= 1
            elif temp_condition % 4 == 2:
                temp_condition += table_data[cond_pos+1][j]
                cond_pos += 1
            elif temp_condition % 4 == 3:
                temp_condition += table_data[cond_pos-1][j]
                cond_pos -= 1
            if cond_pos == table_data[-1] and j == 10:
                count += 1
        except IndexError:
            break
print(count)