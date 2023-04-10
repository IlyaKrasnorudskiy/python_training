from PIL import Image
import os

if not os.path.exists("filtered_images"):
    os.mkdir("filtered_images")

files = ["my_image.jpg", "my_image1.jpg", "my_image2.jpg", "my_image3.jpg", "my_image4.jpg"]

# проходим по каждому файлу
for file in files:
    img = Image.open(file)
    img_grayscale = img.convert('L')
    img_grayscale.save(f"filtered_images/{file[:-4]}_grayscale.jpg")
