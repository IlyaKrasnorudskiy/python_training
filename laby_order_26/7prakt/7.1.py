from PIL import Image

# открываем изображение
image = Image.open("my_image.jpg")

# выводим информацию
print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель:", image.mode)

# отображаем изображение на экране
image.show()
