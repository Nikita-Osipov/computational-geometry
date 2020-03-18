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
rngGray = []
for i in range(256):
    rngR.append(0)   
    rngG.append(0) 
    rngB.append(0) 
    rngGray.append(0) 
for x in range(width):
        for y in range(height):
            a = pix[x, y][0]
            rngR[a] +=1
            b = pix[x, y][1]
            rngG[b] +=1
            c = pix[x, y][2]
            rngB[c] +=1
            s =(a+b+c) // 3
            rngGray[s] +=1
maxR = max(rngR)
maxG = max(rngG)
maxB = max(rngG)
maxGray = max(rngGray)
height2 = height // 2
width2 = width // 2
R = maxR // height2
G = maxG // height2
B = maxB // height2
Gray = maxGray // height2
for i in range(len(rngG)):
    rngR[i] = rngR[i] // R
    rngG[i] = rngG[i] // G
    rngB[i] = rngB[i] // B
    rngGray[i] = rngGray[i] // Gray

for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                if (x <= 255) and (y < int(rngG[x])):
                    draw.point((x, height2 - y), (0, 255, 0))
                elif (x >= width2) and (x < width2 + 256) and (y < int(rngR[x - width2])):
                    draw.point((x, height2 - y), (255, 0, 0))
                elif (x <= 255) and (y > height2) and (y < int(height2 + rngGray[x])):
                    draw.point((x, height-y+height2), (128, 128, 128))
                elif (x >= width2) and (x < width2 + 256) and (y < int(rngB[x - width2]+height2)) and (y > height2):
                    draw.point((x, height-y+height2), (0, 0, 255))
                else:
                    draw.point((x, y), (a, b, c))

image.show()
del draw
 