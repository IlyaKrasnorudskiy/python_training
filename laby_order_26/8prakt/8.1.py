from PIL import Image

# Открываем изображение
image = Image.open('my_image.jpg')

# Обрезаем изображение (левый верхний угол: x1, y1, правый нижний угол: x2, y2)
cropped_image = image.crop((100, 100, 300, 300))

# Сохраняем обрезанное изображение
cropped_image.save('cropped_example.jpg')
