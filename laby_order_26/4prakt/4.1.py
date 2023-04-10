def is_divisible_by_3(number):
    if number % 3 == 0:
        print("Число делится на 3.")
    else:
        print("Число не делится на 3.")

number = int(input("Введите число: "))
is_divisible_by_3(number)