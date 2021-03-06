# Для выполнения практической работы номер 2 используйте ЭТОТ файл
import random,math
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("bear.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def lineP(p1, p2, color):  # рисуем линию из точки p1(x1,y1) в точку p2(x2,y2)
        x1 = p1[0]  # Перекладываем координаты точек в более понятные переменные
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        dX = abs(x2 - x1) # Вычисляем "смещение по X"
        dY = abs(y2 - y1) # Вычисляем "смещение по Y"
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY # "Изменение ошибки"
            y = y1    # текущий Y (начальное значение)
            dirY = sign(y2 - y1) # направление изменения Y
            for x in range(x1, x2 + 1): # перебираем все X от x1 до x2
                    draw.point((x,y),color) # закрашиваем пиксель (x,y)
                    err += dErr             # добавляем "смежение" к "ошибке"
                    if err + err >= dX: # если "ошибка" накопилась
                            y += dirY   # изменяем Y на 1
                            err -= dX   # вычитаем из "ошибки" dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),color)
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY
def triangle (p1, p2, p3, color): # Рисуем треугольник по трем точкам - p1, p2, p3
	# Сейчас здесь вместо заливки треугольника просто рисуются его границы
	# Нужно именно здесь расположить код своей программы, которая будет
	# Закрашивать треугольник
        lst = sorted((p1,p2,p3))        
        ac = lst[1]
        x1 = ac[0]
        y1 = ac[1]
        al = lst[0]
        x2 = al[0]
        y2 = al[1]
        ar = lst[2]
        x3 = ar[0]
        y3 = ar[1]
        k1 = (y1-y2)/(x1-x2)
        k2 = (y3-y1)/(x3-x1)
        k3 = (y3-y2)/(x3-x2)
        b1 = round(y1 - k1*x1)
        b2 = round(y3 - k2*x3)
        b3 = round(y3 - k3*x3)
        if k3*x1+b3<y1:
            n = -1;
        else:
            n = 1;
        for x in range(width):
            for y in range(height): 
                if n == 1:
                    if x <= x1 and x >= x2:
                        ystart = k1*x+b1
                        yend = k3*x+b3
                        if ystart <= y <= yend:
                            draw.point((x, y), color)
                    elif x > x1 and x <= x3:
                        ystart = k2*x+b2
                        yend = k3*x+b3
                        if ystart <= y <= yend:
                            draw.point((x, y), color)    
                            
                else:
                    if x <= x1 and x >= x2:
                        ystart = k3*x+b3
                        yend = k1*x+b1   
                        if ystart <= y <= yend:
                            draw.point((x, y), color)
                    elif x > x1 and x <= x3:
                        ystart = k3*x+b3
                        yend = k2*x+b2
                        if ystart <= y <= yend:
                            draw.point((x, y), color) 
    
            
        
        
    
        lineP(p1, p2, color)
        lineP(p2, p3, color)
        lineP(p1, p3, color)

# В следующих строках задаются цвета треугольников и точки, по которым они строятся
black = (0,0,0)
green = (0,200,0)
red = (200,0,0)
blue = (0,0,200)
t1 = (0,height//4)
t2 = (width//2, 0)
t3 = (width//4, height//2)
t4 = (width-1,height//2)
t5 = (width//2,height//4)
t6 = (width*3//4,0)
t7 = (0,height//2)
t8 = (width//4,height-1)
t9 = (width//2,height*3//4)
t10 = (width-1,height*3//4)
t11 = (width*3//4,height//2)
t12 = (width//2,height-1)
# Ниже вызываем заливку 4-х треугольников для проверки работы программы
triangle(t1, t2, t3, green)
triangle(t4, t5, t6, red)
triangle(t7, t8, t9, blue)
triangle(t10, t11, t12, black)

image.show()
#image.save("result.jpg")
del draw
