alf = "ПЯТНИЦА"
count = 0
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                        slovo = a1+a2+a3+a4+a5
                        if a1 != "Н" and slovo.count("Я") == 1:
                            count = count + 1
print(count)

