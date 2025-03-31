alf = '23'
slovo = ''
count = 0
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        for a7 in alf:
                            slovo = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            if slovo.count('2') > slovo.count('3') and int(slovo) % 3 == 0 and int(slovo) % 4 == 0:
                                print(slovo)

print(count)