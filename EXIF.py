from PIL import Image

img = Image.open("IMG_4187.jpeg")
exif = img.getexif()

for id,value in exif.items():
    print(id,value)