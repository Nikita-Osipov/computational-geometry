from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
	global filled
	filled = 1

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	global filled
	if key == b'\x1b':
		sys.exit(0)
	if key == b' ':
		filled = 1 - filled
	glutPostRedisplay()         # Вызываем процедуру перерисовки

# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
	glRotated(0.125,1,1,1)
	global filled
	if filled == 1:
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	else:
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 


	R = 0.5
        
	glBegin(GL_QUAD_STRIP)
	for j in range(-8, 6):
		R1 = R*cos(pi*j/18)
		z = R*sin(pi*j/18)
		for i in range(21):
			glColor3f(1, 0, 0)
			glVertex3d(R*cos(2*pi*i/20), R*sin(2*pi*i/20), 0)
			glColor3f(0, 0, 1)
			glVertex3d(R1*cos(2*pi*(i+1)/20), R1*sin(2*pi*(i+1)/20), z)
        
	glEnd()
   
	R2 = R*cos(pi*5/18)
	z = R*sin(pi*5/18)
    
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0, 1, 0)
	glVertex3d(0,0,z)
	for k in range(21):
		glVertex3d(R2 * cos(2*pi*k/20),R2 * sin(2*pi*k/20), z)
	glEnd()  

	glBegin(GL_QUAD_STRIP)

	glColor3f(1, 0, 0)
	for k in range(21):
		glVertex3d(R2 * cos(2*pi*k/20),R2 * sin(2*pi*k/20), z)
		glVertex3d(R2 * cos(2*pi*k/20),R2 * sin(2*pi*k/20), 1)
	glEnd() 
    
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0, 0, 1)
	glVertex3d(0,0,z)
	for k in range(21):
		glVertex3d(R2 * cos(2*pi*k/20),R2 * sin(2*pi*k/20), 1)
	glEnd() 


    
	glutSwapBuffers()           # Меняем буферы
	glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
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
