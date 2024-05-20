from PIL import Image
image = Image.open('2.png')
cropped = image.crop((0, 80, 120, 560))
cropped.save('2crop.png')