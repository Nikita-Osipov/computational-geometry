import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

rng = []
for i in range(256):
    rng.append(0)   
for x in range(width):
        for y in range(height):
            b = pix[x, y][1]
            rng[b] +=1
maxN = max(rng)
height2 = height // 2
k = maxN // height2
for i in range(len(rng)):
    rng[i] = rng[i] // k

for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if (x <= 255) and (y < int(rng[x])):
                    draw.point((x, height2 - y), (0, 255, 0))
                else:
                    draw.point((x, y), (a, b, c))

image.show()
del draw
