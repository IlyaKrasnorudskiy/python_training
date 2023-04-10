from PIL import Image

# Открываем изображение
image = Image.open("my_image.jpg")

# Получаем размеры изображения
width, height = image.size

# Создаем уменьшенную копию в 3 раза
new_size = (int(width/3), int(height/3))
small_image = image.resize(new_size)

# Получаем зеркальный горизонтальный образ
mirror_h_image = image.transpose(Image.FLIP_LEFT_RIGHT)

# Получаем зеркальный вертикальный образ
mirror_v_image = image.transpose(Image.FLIP_TOP_BOTTOM)

# Сохраняем изображения в текущую папку
small_image.save("small_image.jpg")
mirror_h_image.save("mirror_h_image.jpg")
mirror_v_image.save("mirror_v_image.jpg")
