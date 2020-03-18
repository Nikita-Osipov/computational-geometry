# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:33:14 2020

@author: Nikita
"""
import random, math
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


class turtle:
    def __init__(self,x,y,a,f,k):
        self.x = x
        self.y = y
        self.a = a
        self.f = f
        self.k = k
        
        def forward(x,y,a,f):
            x1 = round(x + a*math.cos(f*3.14/180))
            y1 = round(y + a*math.sin(f*3.14/180))
            line(x,y,x1,y1)
            self.x = x1
            self.y = y1
            
        def req(x,y,a,k,f):
            if k == 1:
                forward(x,y,a,f)
            else:
                req(self.x,self.y,self.a/3,k-1,f)
                f = f + 60
                req(self.x,self.y,self.a/3,k-1,f)
                f = f - 120
                req(self.x,self.y,self.a/3,k-1,f)
                f = f + 60   
                req(self.x,self.y,self.a/3,k-1,f)
        
        req(self.x,self.y,self.a,self.k,self.f)
        


image = Image.open("test.jpg") #Открываем изображение 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину  
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
        for y in range(height):
                draw.point((x, y), (255, 255, 255))

turtle1 = turtle(width//2,0,20,90,5)
image.show()
#image.save("result.jpg")
del draw



    
