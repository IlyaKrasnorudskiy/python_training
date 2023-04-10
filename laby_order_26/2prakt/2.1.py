password = input("Введите пароль: ")
password_confirmation = input("Подтвердите пароль: ")

if password == password_confirmation:
    print("Пароль принят")
else:
    print("Пароль не принят")