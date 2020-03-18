import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def line(x1, y1, x2, y2):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1)
            for x in range(x1, x2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dX:
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY
def bezie(p0, p1, p2, p3):
	oldBx = p0[0]
	oldBy = p0[1]
	for i in range(101):
		t = i / 100
		Bx = int((1-t)*(1-t)*(1-t)*p0[0] + 3*t*(1-t)*(1-t)*p1[0] + 3*t*t*(1-t)*p2[0] + t*t*t*p3[0])
		By = int((1-t)*(1-t)*(1-t)*p0[1] + 3*t*(1-t)*(1-t)*p1[1] + 3*t*t*(1-t)*p2[1] + t*t*t*p3[1])
		line(oldBx, oldBy, Bx, By)
		oldBx = Bx
		oldBy = By

image = Image.open("roof_half.jpg") #Открываем изображение 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину  
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей 
for x in range(width): 
        for y in range(height):
                draw.point((x, y), (255, 255, 255))
#line(width//4, height//4, width//4, height*3//4)
#line(width*3//4, height//4, width*3//4, height*3//4) 
#bezie((width//2,height), (width,height), (0,0), (width//2,0))
bezie((width//3,0), (width//3,0), (2*width//3,0), (2*width//3,0))
bezie((width//3,height-1), (width//3,height-1), (2*width//3,height-1), (2*width//3,height-1))
#bezie((width//3,0), (width//2,height//2), (0,height//2), (width//3,height))
#bezie((width//3,0), (width//2,height//2), (0,height//2), (width//3,height))
bezie((width//3,0), (4*width//10,height//5), (4*width//10,2*height//5), (width//3,height//2))
bezie((2*width//3,0), (6*width//10,height//5), (6*width//10,2*height//5), (2*width//3,height//2))
bezie((width//3,height//2), (2*width//10,3*height//5), (2*width//10,9*height//10), (width//3,height))
bezie((2*width//3,height//2), (8*width//10,3*height//5), (8*width//10,9*height//10), (2*width//3,height))
image.show() 
#image.save("result.jpg")
del draw
