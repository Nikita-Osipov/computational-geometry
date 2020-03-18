import random, math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("park.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

image2 = Image.open("winter.jpg") #Открываем изображение
draw2 = ImageDraw.Draw(image2) #Создаем инструмент для рисования
width2  = image2.size[0] #Определяем ширину 
height2 = image2.size[1] #Определяем высоту 	
pix2 = image2.load() #Выгружаем значения пикселей

w = width // 3

for x in range(width):
    for y in range(height):
        if x <= w:
            a = pix[x, y][0]
            b = pix[x, y][1]
            c = pix[x, y][2] 
            draw.point((x, y), (a,b,c))
        elif x <= 2*w:
            q = (x - w) / w
            a = round(pix[x, y][0]*(1-q) + pix2[x,y][0]*q)
            b = round(pix[x, y][1]*(1-q) + pix2[x,y][1]*q)
            c = round(pix[x, y][2]*(1-q) + pix2[x,y][2]*q) 
            draw.point((x, y), (a,b,c)) 
        else:
            a = pix2[x, y][0]
            b = pix2[x, y][1]
            c = pix2[x, y][2] 
            draw.point((x, y), (a,b,c))           

image.show()
del draw
