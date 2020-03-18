import random, math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("park.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей


w = width // 6
r = height // 2

x1 = width // 2
y1 = height // 2

r2 = 2*(r // 3)


for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2] 
        q = math.sqrt((x - x1)**2+(y-y1)**2)
        q = q/width          
        if ((x - x1)**2)/x1**2 + ((y - y1)**2)/y1**2 > 1:
            draw.point((x, y), (255,255,255))
        elif ((x - x1)**2)/(x1-w)**2 + ((y - y1)**2)/(y1-w)**2  > 1:
            k = round(q*150)
            draw.point((x, y), (a+k,b+k,c+k))
        else:
            draw.point((x, y), (a,b,c)) 

image.show()
del draw 
