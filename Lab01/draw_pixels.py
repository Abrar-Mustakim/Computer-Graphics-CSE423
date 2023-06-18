import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


#def draw_points(x, y):

def draw_points(a, b):
    glPointSize(6) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(a, b)
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
    #call the draw methods here
    #draw_points()
    for i in range(50):
        a = random.randint(1, 490)
        b = random.randint(1, 490)
        glColor3f(0.01*i, 0.02*i, 0.3*i)
        draw_points(a, b)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Drawing Pixels") #window name
glutDisplayFunc(showScreen)

glutMainLoop()