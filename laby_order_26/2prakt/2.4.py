color1 = input("Введите первый основной цвет: ").lower()
color2 = input("Введите второй основной цвет: ").lower()

if color1 not in ['красный', 'синий', 'желтый'] or color2 not in ['красный', 'синий', 'желтый']:
    print("Ошибка: введены некорректные цвета.")
else:
    if color1 == color2:
        print("Вы ввели одинаковые цвета, вторичный цвет не получится.")
    elif (color1 == 'красный' and color2 == 'синий') or (color1 == 'синий' and color2 == 'красный'):
        print("Получится фиолетовый.")
    elif (color1 == 'красный' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'красный'):
        print("Получится оранжевый.")
    elif (color1 == 'синий' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'синий'):
        print("Получится зеленый.")
