import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

k = height // 4
h = width // 18
for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2] 
        if (x-width // 2)**2+(y-height // 2)**2 <= k**2:
            draw.point((x, y), (255, 70, 0))       
        elif y >= k and y <= height - k and x % h < h // 2:
            draw.point((x, y), (0, 255, 0))
        else:
            draw.point((x, y), (a, b, c))
            
image.show()
del draw
