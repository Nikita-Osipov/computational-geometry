import random, math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

k = height // 4
h = width // 2

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2] 
        if x < h:
            q = x / h   
            draw.point((x, y), (math.floor(a*q), math.floor(b*q), math.floor(c*q)))
        else:
            q = (x - h) / (h//4)
            draw.point((x, y),  (a+math.floor(a*q), b+ math.floor(b*q),c + math.floor(c*q)))
image.show()
del draw
