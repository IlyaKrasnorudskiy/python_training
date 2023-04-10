def is_magic_date(day, month, year):
    return day * month == year % 100

try:
    user_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    day, month, year = map(int, user_date.split('.'))
    if is_magic_date(day, month, year):
        print("Дата является магической!")
    else:
        print("Дата не является магической.")
except ValueError:
    print("Некорректный ввод. Введите дату в формате ДД.ММ.ГГГГ")