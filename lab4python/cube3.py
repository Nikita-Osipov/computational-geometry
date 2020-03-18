from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

"""
	glColor3f(1, 0, 1)
	glVertex3d(0.1,0.1,0.1)
	glVertex3d(0.1,0.1,-0.1)
	glVertex3d(-0.1,0.1,-0.1)
	glVertex3d(-0.1,0.1,0.1)
    
	glColor3f(1, 1, 0)
	glVertex3d(0.1,-0.1,0.1)
	glVertex3d(0.1,-0.1,-0.1)
	glVertex3d(-0.1,-0.1,-0.1)
	glVertex3d(-0.1,-0.1,0.1)

"""      
       
# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	if key == b'\x1b':
		sys.exit(0)
	glutPostRedisplay()         # Вызываем процедуру перерисовки
    
    
def cubes(k):
	c = 0.09*k
	h = 0.2*k
    
	glColor3f(1-c, 0, c)  
	glVertex3d(0.1,1.1-h,0.1)
	glVertex3d(0.1,0.9-h,0.1)
	glVertex3d(-0.1,0.9-h,0.1)
	glVertex3d(-0.1,1.1-h,0.1)
        	
	glVertex3d(0.1,1.1-h,0.1)
	glVertex3d(0.1,0.9-h,0.1)
	glVertex3d(0.1,0.9-h,-0.1)
	glVertex3d(0.1,1.1-h,-0.1)
    
	glVertex3d(0.1,1.1-h,-0.1)
	glVertex3d(0.1,0.9-h,-0.1)
	glVertex3d(-0.1,0.9-h,-0.1)
	glVertex3d(-0.1,1.1-h,-0.1)
            
	glVertex3d(-0.1,1.1-h,-0.1)
	glVertex3d(-0.1,0.9-h,-0.1)
	glVertex3d(-0.1,0.9-h,0.1)
	glVertex3d(-0.1,1.1-h,0.1)
    
	glVertex3d(0.1,0.9-h,0.1)
	glVertex3d(0.1,0.9-h,-0.1)
	glVertex3d(-0.1,0.9-h,-0.1)
	glVertex3d(-0.1,0.9-h,0.1)    
 
# Процедура рисования
def draw(*args, **kwargs):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
	glRotated(0.125,1,1,1)

	glBegin(GL_QUADS)  
    
	for k in range(11):
        		cubes(k)
          
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
