binary_str = '110101'
decimal_num = 0
for i in range(len(binary_str)):
    decimal_num += int(binary_str[i]) * 2**(len(binary_str)-i-1)

print(decimal_num)