import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_quads(a, b):   #200,0
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(a, b)  # starting point of trunk  #200,0
    glVertex2f(a+200, b) #400, 0
    glVertex2f(a+200, b) #400, 0
    glVertex2f(a+200, a)  #400, 200
    glVertex2f(a+200, a)  #400, 200
    glVertex2f(a, a)   #200, 200
    glVertex2f(a, a)   #200, 200
    glVertex2f(a, b) #400, 0
    #glVertex2f(a+200, a)  #400, 200
    #glVertex2f(a+200, b) #400, 0
    glEnd()


def window(a, b):   #210, 100
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(a, b)  # starting point of trunk   #210, 100
    glVertex2f(a+50, b)   #260, 100
    glVertex2f(a+50, b)   #260, 100
    glVertex2f(a+50, b+50)   #260, 150
    glVertex2f(a+50, b+50)   #260, 150
    glVertex2f(a, b+50)     #210, 150
    glVertex2f(a, b+50)     #210, 150
    glVertex2f(a, b) 
    glEnd()

def door(a, b):   #270, 0
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(a, b)  # starting point of trunk #270, 0
    glVertex2f(a+50, b)       #320, 0
    glVertex2f(a+50, b)       #320, 0
    glVertex2f(a+50, b+100)   #320, 100
    glVertex2f(a+50, b+100)   #320, 100
    glVertex2f(a, b+100)      #270, 100
    glVertex2f(a, b+100)      #270, 100
    glVertex2f(a, b)
    glEnd()
'''
def draw_triangle():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(200, 200)  # starting point of trunk
    glVertex2f(300, 350)
    glVertex2f(300, 350)
    glVertex2f(400, 200)
    glEnd()
'''
def draw_triangle():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 200)  # starting point of trunk
    glVertex2f(400, 200)
    glVertex2f(300, 350)
    
    
    glEnd()

def draw_points(a, b):
    glPointSize(5) #pixel size. by default 1 thake
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
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points()
    #for i in range(50):
    #    a = random.randint(0, 500)
    #    b = random.randint(0, 500)
    #    draw_points(a, b)
    draw_quads(200, 0)

    glColor3f(1.0, 0.0, 0.0)  # konokichur color set (RGB)
    window(210, 100)
    glColor3f(1.0, 0.0, 0.0)
    window(340, 100)
    glColor4f(1.0, 1, 0.0, 0.0)
    draw_triangle()
    glColor3f(0.0, 1.0, 0.0)
    door(270, 0)
    glColor3f(1.0, 0.0, 1.0)
    draw_points(310, 50)
    # call the draw methods here
    # draw_points()
    # for i in range(50):
    #    a = random.randint(0, 500)
    #    b = random.randint(0, 500)
    #    draw_points(a, b)
    #draw_quads(150, 250)
    #draw_triangle()
    #draw_points(300, 300)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"20301125 House Building") #window name
glutDisplayFunc(showScreen)

glutMainLoop()