import os
from PIL import Image

# Создаем словарь пар "название праздника - имя файла"
cards = {
    'День Рождения': 'my_image.jpg',
    'Новый Год': 'my_image1.jpg',
    'День Святого Валентина': 'my_image2.jpg'
}

# Запрашиваем у пользователя название праздника
holiday = input('Введите название праздника: ')

# Получаем имя файла открытки для выбранного праздника
filename = cards.get(holiday)

# Если такого праздника нет в словаре, сообщаем об этом
if filename is None:
    print('Открытки для данного праздника нет')
else:
    # Получаем полный путь до файла открытки
    filepath = os.path.join('cards', filename)

    # Открываем файл открытки
    with Image.open(filepath) as img:
        # Отображаем открытку
        img.show()
