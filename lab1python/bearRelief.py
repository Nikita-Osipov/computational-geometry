import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("bear.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

ss = 128

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        s = (a+b+c) // 3
        if x < width - 1:
            a1 = pix[x+1, y][0]
            b1 = pix[x+1, y][1]
            c1 = pix[x, y][2]
            s1 = (a1+b1+c1) // 3  
            k = s - s1           
            draw.point((x, y), (ss+4*k,ss+4*k,ss+4*k))
        else:
            draw.point((x, y), (ss,ss,ss))

            
image.show()
del draw
