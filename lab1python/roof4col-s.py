import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

s1 = 255 // 3
s2 = 255 // 6
s3 = 3*s2
s4 = 5*s2 

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        s = (a+b+c) // 3
        if s <= s2:
            draw.point((x, y), (0,0,0))
        elif s <= s3:
            draw.point((x, y), (s1,s1,s1))
        elif s <= s4:
            draw.point((x, y), (2*s1,2*s1,2*s1))
        else:
            draw.point((x, y), (255,255,255))
            
image.show()
del draw
 