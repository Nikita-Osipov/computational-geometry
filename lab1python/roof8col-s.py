import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

s = 255

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        if a <= 128:
            a = 0
        else:
            a = 255
        if b <= 128:
            b = 0
        else:
            b = 255
        if c <= 128:
            c = 0
        else:
            c = 255          
        draw.point((x, y), (a,b,c))

            
image.show()
del draw
 