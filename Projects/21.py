import random

tuz = 11
n = 100
k = 1000
print('Приветствую в честной карточной игре 21 ', 'Ваш баланс=', n)
print('Цель: дойти до ', k)
print('Желаю удачи!')
while k > n:
    # Карточная колода из 36 карт
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, tuz] * 4
    diler = 0
    player = 0
    tuz = 11
    a = input('Сделайте ставку: ')
    if int(n) >= int(a):
        # Дилер берет первую карту
        di1 = random.choice(koloda)
        diler += di1
        print(di1, '-diler')
        del koloda[di1]
    else:
        print('У вас недостаточно средств')
        break
    # Дилер берет вторую карту
    di2 = random.choice(koloda)
    if di1 + di2 == 22:
        diler = 21
        print(di2, '-diler')
        del koloda[di2]
    else:
        diler += di2
        print(di2, '-diler')
        del koloda[di2]
    # Игрок берет первую карту
    pi1 = random.choice(koloda)
    player += pi1
    print(pi1, '-player')
    del koloda[pi1]
    # Игрок берет вторую карту
    pi2 = random.choice(koloda)
    if pi1 + pi2 == 22:
        player = 21
        print(pi2, '-player')
        del koloda[pi2]
    else:
        player += pi2
        print(pi2, '-player')
        del koloda[pi2]

    # Набор игрока
    print('Счет', diler, ':', player)
    while player < 21:
        vopr = input('Еще?(да или нет)')
        if vopr == 'нет':
            break
        elif vopr == 'да':
            pi = random.choice(koloda)
            print('Счет: ', diler, ' : ', player, )
            if pi == tuz and player >= 11:
                player += 1
                print('Вы берете: 1')
                print('Счет: ', diler, ' : ', player, )
                del koloda[pi]
            else:
                player += pi
                print('Вы берете: ', pi)
                del koloda[pi]
                print('Счет: ', diler, ' : ', player, )
    # Проверка на золотое очко
    if diler == 21 and player != 21:
        n = int(n) - int(a)
        print(diler, ' : ', player, ' | ВЫ ПРОИГРАЛИ')
        print('Ваш баланс =', n)
        continue
    elif player == 21 and diler != 21:
        n = int(n) + int(a)
        print(diler, ' : ', player, ' | ВЫ ВЫИГРАЛИ')
        print('Ваш баланс =', n)
        continue

    # Проверка на перебор игрока
    if player > 21:
        n = int(n) - int(a)
        print('У Вас перебор')
        print(diler, ' : ', player, ' | ВЫ ПРОИГРАЛИ')
        print('Ваш баланс =', n)
        print('*' * 5)
        continue
    # Набор дилера
    while diler < player:
        di = random.choice(koloda)
        if di == tuz and diler >= 11:
            print('Дилер берет: ', di, ' , и берет за 1')
            diler += 1
        else:
            print('Дилер берет: ', di)
            diler += di

    # Проверка на перебор дилера и усл.
    if diler > 21 and diler > player:
        n = int(n) + int(a)
        print('Перебор у дилера!')
        print(diler, ' : ', player, '| ВЫ ВЫИГРАЛИ')
        print('Ваш баланс =', n)
        print('*' * 5)
    elif diler == player:
        n = n
        print('| Ничья')
        print('Ваш баланс =', n)
        print('*' * 5)
    elif diler < player:
        n = int(n) + int(a)
        print(diler, ' : ', player, '| ВЫ ВЫИГРАЛИ')
        print('Ваш баланс =', n)
        print('*' * 5)
    elif diler > player:
        n = int(n) - int(a)
        print(diler, ' : ', player, '| ВЫ ПРОИГРАЛИ ')
        print('Ваш баланс =', n)
        print('*' * 5)
        if n == 0:
            print(diler, ' : ', player, 'Вы проиграли всё')


