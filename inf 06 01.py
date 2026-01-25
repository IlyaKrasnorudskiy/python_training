from itertools import permutations
count = 0
for code in permutations("01234567", r = 5):
    if int(code[0]) % 2 != int(code[1]) % 2 and int(code[1]) % 2 != int(code[2]) % 2:
        if int(code[2]) % 2 != int(code[3]) % 2 and int(code[3]) % 2 != int(code[4]) % 2:
            if code.count('1') == 0 and code[0] != '0':
                count+=1
print(count)
