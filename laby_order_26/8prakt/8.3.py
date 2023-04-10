from PIL import Image, ImageDraw, ImageFont

# Получаем имя и фото из словаря
cards = {
    'День Рождения': 'my_image.jpg',
    'Новый Год': 'my_image1.jpg',
    'День Святого Валентина': 'my_image2.jpg'
}

holiday = input("Введите название праздника: ")
if holiday not in cards:
    print("Такой праздник отсутствует в списке")
else:
    name = input("Введите имя получателя: ")

    # Открываем изображение
    image = Image.open(cards[holiday])

    # Создаем объект ImageDraw и объект шрифта
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=50)

    # Получаем размер текста и центрируем его
    text = f"{name}, поздравляю!"
    text_width, text_height = draw.textsize(text, font)
    x = (image.width - text_width) / 2
    y = image.height * 0.1

    # Рисуем текст на изображении
    draw.text((x, y), text, font=font, fill=(255, 0, 0), align='center', stroke_width=2, stroke_fill=(0, 0, 0), font_weight='bold')

    # Сохраняем новое изображение в формате png
    image.save(f"{holiday}_{name}.png", "PNG")
