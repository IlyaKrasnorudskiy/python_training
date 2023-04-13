from PIL import Image, ImageDraw, ImageFont
import os

# Список файлов
files = ["my_image.jpg", "my_image1.jpg", "my_image2.jpg"]

# Цикл по списку файлов
for filename in files:
    # Открываем изображение и создаем объект ImageDraw
    im = Image.open(filename)
    draw = ImageDraw.Draw(im)

    # Определяем размер изображения
    width, height = im.size

    # Загружаем шрифт и создаем объект ImageFont
    font = ImageFont.truetype("arial.ttf", 36)

    # Добавляем текст в центр изображения
    text = "Watermark"
    textwidth, textheight = draw.textbbox((0, 0, width, height), text, font=font)
    x = (width - textwidth) / 2
    y = (height - textheight) / 2
    draw.text((x, y), text, font=font)

    # Получаем новое имя файла
    new_filename = os.path.splitext(filename)[0] + "_watermarked.jpg"

    # Сохраняем изображение
    im.save(new_filename)