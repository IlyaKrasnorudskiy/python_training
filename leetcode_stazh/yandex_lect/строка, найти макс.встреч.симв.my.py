s = "-1ssadsafgsdgsdfgh-53чZXCVS#khg45:#:psasasssgghbcxbxhrtdfagdsasdgcvx"
symb_count = {}
symbol = s[0]
temp = 0
for i in range(len(s)):
    if s[i] not in symb_count:
        symb_count[s[i]] = 1
    else:
        symb_count[s[i]] += 1
    if symb_count[s[i]] > temp:
        temp = symb_count[s[i]]
        symbol = s[i]
print(symbol)
#В красивом решении, используют не индексированный цикл по строке, а берут сам символ. В теле первого условия можно
#Закидывать новые символы со значением 0 и по выходу из тела условия, инкрементировать по ключу значение.