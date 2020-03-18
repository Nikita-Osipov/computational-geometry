import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("lego.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

rngR = []
rngG = []
rngB = []

for i in range(256):
    rngR.append(0)   
    rngG.append(0) 
    rngB.append(0) 
    
for x in range(width):
        for y in range(height):
            a = pix[x, y][0]
            rngR[a] +=1
            b = pix[x, y][1]
            rngG[b] +=1
            c = pix[x, y][2]
            rngB[c] +=1

maxR = max(rngR)//100
maxG = max(rngG)//100
maxB = max(rngG)//100

Rmin = 0
Rmax = 0

Gmin = 0
Gmax = 0

Bmin = 0
Bmax = 0

for i in range(255):
    if rngR[i+1]-rngR[i] > 1*maxR:
        Rmin = i+1
        break
        
for i in reversed(range(1,256)):
    if rngR[i-1]-rngR[i] > 1*maxR:
        Rmax = i-1
        break

for i in range(255):
    if rngG[i+1]-rngG[i] > 1*maxG:
        Gmin = i+1
        break
    
for i in reversed(range(1,256)):
    if rngG[i-1]-rngG[i] > 1*maxG:
        Gmax = i-1
        break

for i in range(255):
    if rngB[i+1]-rngB[i] > 1*maxB:
        Bmin = i+1
        break
    
for i in reversed(range(1,256)):
    if rngB[i-1]-rngB[i] > 1*maxB:
        Bmax = i-1
        break

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2] 
        if a < Rmin:
            a = 0
        elif a > Rmax:
            a = 255
        else:
            a = round(((a - Rmin)/(Rmax - Rmin))*255)
        if b < Gmin:
            b = 0
        elif b > Gmax:
            b = 255
        else:
            b = round(((b - Gmin)/(Gmax - Gmin))*255 )
        if c < Bmin:
            c = 0
        elif c > Bmax:
            c = 255
        else:
            c = round(((c - Bmin)/(Bmax - Bmin))*255   )   
        draw.point((x, y), (a,b,c))
          
image.show()
del draw
