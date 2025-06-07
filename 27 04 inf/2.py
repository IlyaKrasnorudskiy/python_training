n = int(input())
slovar = {}
for i in range(0, n*2):
    fio = str(input())
    num = int(input())
    if fio not in slovar :
        slovar[fio] = 0
        if num == 5:
            slovar[fio]+=1
    else:
        if num == 5:
            slovar[fio] += 1
for i in range(0, len(slovar)):
    if slovar[i].value =

