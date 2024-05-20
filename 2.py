from PIL import Image
a={"День рождения": "С днем рождения.jpeg", "Новый год": "С новым годом.jpeg", "8 марта": ""}
b=input("Введите название праздника ")

if b in a:
    c = a[b]
    photo = Image.open(c)
    photo.show()
else:
    print("Открытки для данного праздника нет")

