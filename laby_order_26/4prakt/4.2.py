def divide_100(number):
    return 100 / number

try:
    user_number = float(input("Введите число: "))
    result = divide_100(user_number)
    print("100 деленное на", user_number, "равно", result)
except ValueError:
    print("Введено некорректное значение. Введите число.")
except ZeroDivisionError:
    print("Деление на ноль невозможно.")
