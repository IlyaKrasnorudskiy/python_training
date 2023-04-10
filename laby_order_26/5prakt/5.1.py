numbers = [3, 7, 12, 23, 42]

user_number = int(input("Введите число: "))

if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")

print("Исходный список чисел:", numbers)
print("Число пользователя:", user_number)
