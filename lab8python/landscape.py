from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(1.0, 1.0, 1.0, 1.0) # Белый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
	global anglex, angley, anglez, filled
	anglex = 0
	angley = 0
	anglez = 0
	filled = 0

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	global anglex, angley, anglez, filled
	if key == b'\x1b':
		sys.exit(0)
	if key == b'w':
		anglex += 5
	if key == b's':
		anglex -= 5
	if key == b'q':
		angley += 5
	if key == b'e':
		angley -= 5
	if key == b'a':
		anglez += 5
	if key == b'd':
		anglez -= 5
	if key == b' ':
		filled = 1 - filled
	glutPostRedisplay()         # Вызываем процедуру перерисовки


array = []

n = 11
k = -1
h = [] 
step = 0.14 
while k < 1:
	array.append([0]*(1+int(2/step)))
	h.append(round(k,3))
	k += step
    
w = h

for i in range(len(h)):
	for j in range(len(h)):
		array[i][j] = round(random.uniform(-0.1,0.1),2)      

# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
	glLoadIdentity()
	global anglex, angley, anglez, filled
	glRotated(anglex,1,0,0)
	glRotated(angley,0,1,0)
	glRotated(anglez,0,0,1)
	glRotated(-105,1,0,0)
	if filled == 1:
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	else:
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        
	for i in range(1,len(h)-1,2):
		for j in range(1,len(w)-1,2):
			glBegin(GL_TRIANGLE_FAN)            
			glColor3f(1,abs(array[i][j]),1)
			glVertex3d(h[i],array[i][j],w[j])
			glVertex3d(h[i]-step,array[i-1][j],w[j])
			glVertex3d(h[i]-step,array[i-1][j+1],w[j]+step)
			glVertex3d(h[i],array[i][j+1],w[j]+step)
			glVertex3d(h[i]+step,array[i+1][j+1],w[j]+step)
			glVertex3d(h[i]+step,array[i+1][j],w[j])
			glVertex3d(h[i]+step,array[i+1][j-1],w[j]-step)
			glVertex3d(h[i],array[i][j-1],w[j]-step)
			glVertex3d(h[i]-step,array[i-1][j-1],w[j]-step)
			glVertex3d(h[i]-step,array[i-1][j],w[j])
			glEnd()
    

	glutSwapBuffers()           # Меняем буферы
	glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
