#Баккарат 52 карты
import random
balance = 1000
print('Ваш баланс составляет:', balance)
#Ф-я набора карт
koloda = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def nabor(j):
    cards = []
    sums = 0
    for i in range(0,j):
        a = random.choice(koloda)
        sums+=a
        cards.append(a)
        koloda.remove(a)
    print(cards)
    return cards
while balance > 0:
    if len(koloda) < 7 :
        koloda = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        print("ПРОИЗОШЛА ЗАМЕНА КОЛОДЫ")
    if balance > 10000:
        print('Поздравляю! Вы прошли игру')
    print("Сделайте ставку ")
    stavka = int(input())
    if stavka > balance and stavka > 0:
        print('У вас нет столько денег!')
        break
    print("На кого ставим? Игрок или Дилер?")
    choice = str(input())
    player = nabor(2)
    diler = nabor(2)
    sumkp = player[0]+player[1]
    sumkd = diler[0]+diler[1]
    if sumkp > 9:
        sumkp = sumkp%10
    if sumkd > 9:
        sumkd = sumkd%10
    if sumkp == sumkd:
        sumkp += int(nabor(1)[0])
        sumkd += int(nabor(1)[0])
    if sumkp > 9:
        sumkp = sumkp%10
    if sumkd > 9:
        sumkd = sumkd%10
    if (choice =='игрок' or choice =='Игрок' or choice =='Buhjr' or choice =='buhjr' or choice =='и'):
        if sumkp > sumkd:
            balance += stavka
            print('ИГРОК', sumkp, ' Дилер', sumkd)
            print('Выигрыш, ', balance)
        else:
            balance -= stavka
            print('ИГРОК', sumkp, ' Дилер', sumkd)
            print('Проигрыш, ', balance)
    if (choice =='дилер' or choice =='Дилер' or choice =='Lbkth' or choice =='lbkth' or choice =='д'):
        if sumkp < sumkd:
            balance += stavka
            print('ИГРОК', sumkp, ' Дилер', sumkd)
            print('Выигрыш, ', balance)
        else:
            balance -= stavka
            print('ИГРОК', sumkp, ' Дилер', sumkd)
            print('Проигрыш, ', balance)
    if sumkp == sumkd:
        print('Ничья', balance)
