count = 0
alf = "ТИМОФЕЙ"
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    slovo = a1+a2+a3+a4+a5
                    if slovo.count('Й')<=1 and slovo[0]!='Й' and slovo[-1]!='Й' and slovo.count('ИЙ')==0 and slovo.count('ЙИ')==0:
                        count +=1
print(count)