from PIL import Image
image = Image.open('2.jpg')
cropped = image.crop((0, 100, 30, 860))
cropped.save('2crop.jpg')

from PIL import Image

a=input("К какому празднику нужна открытка? ")
dictionary = {"Новый год": "нг.jpg", "8 марта": "8.jpg","Пасха": "пасха.jpg"}

if a in dictionary:
    b = dictionary[a]
    dictionary = Image.open(b)
    dictionary.show()
else:
    print("Извините, открытки для данного праздника не найдено.")

from PIL import Image, ImageDraw, ImageFont

dictionary = {
    "Новый год": "нг.jpg",
    "Пасха": "пасха.jpg",
    "8 марта": "8.jpg"
}

a = input("К какому празднику вам нужна открытка? ")
имя = input("Кого вы хотите поздравить? ")

if a in dictionary:
    b = dictionary[a]
    открытка = Image.open(b)

    draw = ImageDraw.Draw(открытка)
    шрифт = ImageFont.truetype("Intro.ttf", 30)
    текст = f"{имя}, поздравляю!"
    draw.text((100, 50), текст, fill="black", font=шрифт)

    newf = "new.png"
    открытка.save(newf)

    print(f"Открытка с текстом сохранена в файле: {newf}")
else:
    print("Извините, открытки для данного праздника не найдено.")