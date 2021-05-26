from PIL import Image

img = Image.open(filename)#.jpeg/jpgどちらでも可能
exif = img.getexif()

for id,value in exif.items():
    print(id,value)