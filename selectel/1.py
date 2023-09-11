str1 = str(input("Введите первую строку: "))
str2 = str(input("Введите вторую строку: "))

def proc_str(string):
    mas = []
    for symbol in string:
        if symbol != "#":
            mas.append(symbol)
        else:
            if mas:
                mas.pop()
        a = ''.join(mas)
        print(a)
    print(string + ' выход : ' + a)
    return ''.join(mas)

def result(string1, string2):
    return proc_str(string1) == proc_str(string2)


print("true" if result(str1, str2) else "false" )
