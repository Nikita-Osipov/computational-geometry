import random, math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей


for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2] 
        s = (a+b+c)//3
        if s > 120:
            draw.point((x, y), (255,255,255))
        else:
            draw.point((x, y), (0,0,0))

image.show()
del draw
