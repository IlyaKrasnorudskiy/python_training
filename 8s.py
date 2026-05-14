from itertools import permutations
count = 0
for i in range(1,11):
    for word in permutations('0123456789', r = i):
        if word[0] != '0':
            if word[-1] == '0' or word[-1] == '5':
                count += 1
print(count+1)