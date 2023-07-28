from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

#Midpoint Line Drawing Algorithms
def midpointcircle(x, y, r):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    #N, S, E, W from center
    d = 1.25-r
    x1 = x 
    y1 = y
    x = 0 
    y = r 
    if x1 != 0 or y1!=0:
        glVertex2f(x+x1, y+y1)
        glVertex2f(y+y1, x+x1)
        glVertex2f(y+y1, -x+x1)
        glVertex2f(x+x1, -y+y1)
        glVertex2f(-x+x1, -y+y1)
        glVertex2f(-y+y1, -x+x1)
        glVertex2f(-y+y1, x+x1)
        glVertex2f(-x+x1, y+y1)
    else: 
        glVertex2f(x, y)
        glVertex2f(y, x)
        glVertex2f(y, -x)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)
        glVertex2f(-y, x)
        glVertex2f(-x, y)
    while x <= y:
        if d<0:
            #E
            d = d+2*x+3 
            x += 1  
        else:
            d = d + 2*x - 2*y + 5
            x = x + 1 
            y = y - 1 
        if x1 != 0 or y1!=0:
            glVertex2f(x+x1, y+y1)
            glVertex2f(y+y1, x+x1)
            glVertex2f(y+y1, -x+x1)
            glVertex2f(x+x1, -y+y1)
            glVertex2f(-x+x1, -y+y1)
            glVertex2f(-y+y1, -x+x1)
            glVertex2f(-y+y1, x+x1)
            glVertex2f(-x+x1, y+y1)
        else: 
            glVertex2f(x, y)
            glVertex2f(y, x)
            glVertex2f(y, -x)
            glVertex2f(x, -y)
            glVertex2f(-x, -y)
            glVertex2f(-y, -x)
            glVertex2f(-y, x)
            glVertex2f(-x, y)
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
    glColor3f(0.5, 0.5, 1.0) #konokichur color set (RGB)
    x, y, r = 250, 250, 200
    midpointcircle(x, y, r)
    r1 = r//2 
    #N, S, E, W axis Circle
    midpointcircle(x+r1, y, r1)
    midpointcircle(x-r1, y, r1)
    midpointcircle(x, y+r1, r1)
    midpointcircle(x, y-r1, r1)
    #Corners Circle
    rs = math.sqrt((r1**2)/2)
    midpointcircle(x+rs, y+rs, r1)
    midpointcircle(x-rs, y-rs, r1)
    midpointcircle(x-rs, y+rs, r1)
    midpointcircle(x+rs, y-rs, r1)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(f"20301125: Midpoint Circle") #window name
glutDisplayFunc(showScreen)
glutMainLoop()