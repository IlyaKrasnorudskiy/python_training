alf = 9
slovo1 = ''
slovo2 = ''
count = 0
for a1 in range(0,alf):
    for a3 in range(0,alf):
        for a4 in range(0,alf):
            for a5 in range(0, alf):
                slovo1 = ''
                slovo2 = ''
                slovo1 = '6' + str(a1)
                slovo2 = str(a3) + str(a4) + str(a5)
                proverka = str(int(slovo1) * int(slovo2))
                if len(proverka) == 4 and proverka[-1] == '6' and a3 != 0 and a5 < 2:
                    print(proverka, slovo1, slovo2)

