seat_number = int(input("Введите номер места: "))

if 1 <= seat_number <= 54:
    if (seat_number - 1) % 4 < 2:
        place = "нижнее"
    else:
        place = "верхнее"

    if (seat_number - 1) % 8 < 4:
        place += " в купе"
    else:
        place += " боковое"
else:
    place = "не существует"

print("Тип места:", place)