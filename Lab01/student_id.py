import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def draw_line():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(250, 150)  # starting point of trunk
    glVertex2f(150, 250)
    glVertex2f(250, 150)  # starting point of trunk
    glVertex2f(350, 150)
    glVertex2f(150, 250)  # starting point of trunk
    glVertex2f(250, 350)
    glVertex2f(250, 350)  # starting point of trunk
    glVertex2f(350, 350)
    glVertex2f(350, 350)
    glVertex2f(450, 250)
    glVertex2f(450, 250)
    glVertex2f(350, 150)
    glEnd()
def draw_two(x=100, a=100, b=200, c=70, d=50):
    glPointSize(10) 
    glBegin(GL_LINES)
    glVertex2f(x, a)  
    glVertex2f(b, a)
    glVertex2f(b, a)  
    glVertex2f(b, c)
    glVertex2f(b, c)  
    glVertex2f(x, c)
    glVertex2f(x, c)  
    glVertex2f(x, d)
    glVertex2f(b, d)  
    glVertex2f(x, d)
    glEnd()

def draw_zero(a=210, b=250, c=100, d=50):
    glPointSize(10) 
    glBegin(GL_LINES)
    glVertex2f(a, c) 
    glVertex2f(b, c)
    glVertex2f(b, c)
    glVertex2f(b, d)
    glVertex2f(b, d)
    glVertex2f(a, d)
    glVertex2f(a, d)
    glVertex2f(a, c)    
    glEnd()

def draw_three(a=260, b=290, c=100, d=50):
    glPointSize(10) 
    glBegin(GL_LINES)
    glVertex2f(a, c) 
    glVertex2f(b, c)
    glVertex2f(b, c)
    glVertex2f(b, d)
    glVertex2f(a, c-30)
    glVertex2f(b, c-30)
    glVertex2f(b, d)
    glVertex2f(a, d)
        
    glEnd()

def draw_one(a=350, c=100, d=50):
    glPointSize(10) 
    glBegin(GL_LINES)
    glVertex2f(a, c) 
    glVertex2f(a, d)
    glEnd()

def draw_five(x=100, a=100, b=200, c=70, d=50):
    glPointSize(10) 
    glBegin(GL_LINES)
    glVertex2f(x, a)  
    glVertex2f(b, a)
    glVertex2f(x, a)  
    glVertex2f(x, c)
    glVertex2f(b, c)  
    glVertex2f(x, c)
    glVertex2f(b, c)  
    glVertex2f(b, d)
    glVertex2f(b, d)  
    glVertex2f(x, d)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    draw_two()
    glColor3f(0.0, 1.0, 0.0)
    draw_zero()
    glColor4f(1.0, 0.5, 0.0, 0.0)
    draw_three()
    glColor3f(0.0, 0.0, 1.0)
    draw_zero(300, 340)
    glColor3f(0.5, 0.5, 0.5)
    draw_one()
    glColor3f(2.0, 0.5, 1.0) #lillac
    draw_one(a=360)
    glColor3f(0.5, 1.0, 1.0)
    draw_two(x=370, b=400)
    glColor4f(1.0, 1.0, 1.0, 0.0) #CMYK
    draw_five(x=410, b=450)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID") #window name
glutDisplayFunc(showScreen)

glutMainLoop()