count = 0
alf = "12345678"
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        for a7 in alf:
                            for a8 in alf:
                                for a9 in alf:
                                    number = a1+a2+a3+a4+a5+a6+a7+a8+a9
                                    if (int(a1) - int(a2)) %2 !=0 and (int(a2) - int(a3)) %2 !=0 and (int(a3) - int(a4)) %2 !=0 and (int(a4) - int(a5)) %2 !=0 and (int(a6) - int(a7)) %2 !=0 and (int(a7) - int(a8)) %2 !=0 and (int(a8) - int(a9)) %2 !=0:
                                        if number.count("1") and number.count("2") and number.count("3") and number.count("4") and number.count("5") and number.count("6") and number.count("7") and number.count("8"):
                                            count+=1
print(count)