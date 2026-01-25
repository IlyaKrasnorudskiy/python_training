from itertools import product
count = 0
for code in product("012345678", repeat = 5):
    index = 0
    if code.count("5") == 1:
        index = code.index("5")
        if code[0] != "0":
            if index != 0 and index !=4:
                if code[index+1] not in "1357" and code[index-1] not in "1357":
                    count+=1
            elif index == 0:
                if code[index + 1] not in "1357":
                    count += 1
            elif index == 4:
                if code[index -1] not in "1357":
                    count += 1
print(count)