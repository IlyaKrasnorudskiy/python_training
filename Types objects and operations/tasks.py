#Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет, имеется ли подстрока subst в строке st.
#В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
#Должно быть найдено совпадение независимо от регистра обеих строк.
def search_substr(subst, st):
    if subst in st:
        print("Есть контакт!")
    else:
        print("Мимо!")
subst = 'как'
st = 'Привет, как дела?'
search_substr(subst, st)

#Требуется определить индексы первого и последнего вхождения буквы в строке.
#Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, st – целевая строка.
#В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть, то кортеж будет состоять из первого и последнего индекса этого символа.
def first_last(letter, st):
    a = []
    for i in range(0, len(st)):
        if letter == st[i]:
            a.append(i)
    return a

letter = 'b'
st = 'absasbsa'
print(first_last(letter, st))


#Вводится целое число. Вывести число, обратное введенному по порядку составляющих его цифр. Например, введено 3425, надо вывести 5243.
number = int(input("pls input number: "))
line = str(number)
print(line[::-1])
