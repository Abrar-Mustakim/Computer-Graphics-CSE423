from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Eight Ways Symmetry
def find_zone(x1, y1, x2, y2):
    dx = x2 - x1 
    dy = y2 - y1 
    if dx > 0 and dy > 0 and abs(dx)>abs(dy):
        return 0 
    elif dx > 0 and dy > 0 and abs(dy) > abs(dx):
        return 1 
    elif dx < 0 and dy > 0 and abs(dy) > abs(dx):
        return 2 
    elif dx < 0 and dy > 0 and abs(dx) > abs(dy):
        return 3 
    elif dx < 0 and dy < 0 and abs(dx) > abs(dy):
        return 4   
    elif dx < 0 and dy < 0 and abs(dy) > abs(dx):
        return 5 
    elif dx > 0 and dy < 0 and abs(dy) > abs(dx):
        return 6 
    elif dx > 0 and dy < 0 and abs(dx) > abs(dy):
        return 7 

#Zone Convert to Zone 0
def convert_zone(X, Y, zone):
    if zone == None:
        x=X
        y=Y
    if zone==0:
        x = X
        y = Y
    if zone==1:
        x = Y
        y = X  
    elif zone==2:
        x = Y
        y = -X 
    elif zone==3:
        x = -X 
        y = Y 
    elif zone==4:
        x = -X 
        y = -Y 
    elif zone==5:
        x = -Y 
        y = -X 
    elif zone==6:
        x = -Y 
        y = X 
    elif zone==7:
        x = X 
        y = -Y 
    return x, y

#Midpoint Line Drawing Algorithms
def midpointLine(x1, y1, x2, y2):
    glPointSize(4) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    dy = y2-y1  
    dx = x2-x1 
    zone = find_zone(x1, y1, x2, y2)
    x = x1 
    y = y1
    x3, y3 = convert_zone(x, y, zone=zone)
    glVertex2f(x3, y3)
    if abs(dx)>=abs(dy):
        d = 2*dy - dx
        E = 2 * dy 
        NE = 2*(dy-dx)
        while (x < x2):
            if d > 0:
                d = d + NE
                x += 1 
                y += 1  
            else: 
                d = d + E  
                x += 1 
            x3, y3 = convert_zone(x, y, zone=zone)
            glVertex2f(x3, y3)
    else:
        d = 2*dx - dy
        E = 2 * dx 
        NE = 2*(dx-dy)
        while (y < y2):
            if d > 0:
                d = d + NE
                x += 1 
                y += 1  
            else: 
                d = d + E  
                y += 1 
            x3, y3 = convert_zone(x, y, zone=zone)
            glVertex2f(x3, y3)
    glEnd()

def letters(inputs, a=150, b=300, c=10, d=100, e=200):
    if inputs == "0":
        midpointLine(a, c, b, c)
        midpointLine(a, c, a, e) 
        midpointLine(b, c, b, e) 
        midpointLine(a, e, b, e)
    if inputs == "1":
        midpointLine(a, c, a, e)
    if inputs == "2":
        midpointLine(a, c, b, c)
        midpointLine(a, c, a, d) 
        midpointLine(a, d, b, d)
        midpointLine(b, d, b, e)
        midpointLine(a, e, b, e)
    if inputs == "3":
        midpointLine(a, c, b, c)
        midpointLine(b, c, b, d) 
        midpointLine(a, d, b, d)
        midpointLine(b, d, b, e)
        midpointLine(a, e, b, e)
    if inputs == "4":
        midpointLine(a, d, a, e) 
        midpointLine(b, c, b, d) 
        midpointLine(a, d, b, d)
        midpointLine(b, d, b, e)
    if inputs == "5":
        midpointLine(a, c, b, c)
        midpointLine(a, d, a, e) 
        midpointLine(b, c, b, d) 
        midpointLine(a, d, b, d)
        midpointLine(a, e, b, e)
    if inputs == "6":
        midpointLine(a, c, b, c)
        midpointLine(a, c, a, d) 
        midpointLine(a, d, a, e) 
        midpointLine(b, c, b, d) 
        midpointLine(a, d, b, d)
        midpointLine(a, e, b, e)
    if inputs == "7": 
        midpointLine(b, c, b, e) 
        midpointLine(a, e, b, e)
    if inputs == "8":
        midpointLine(a, c, b, c)
        midpointLine(a, c, a, d) 
        midpointLine(a, d, a, e) 
        midpointLine(b, c, b, d) 
        midpointLine(a, d, b, d)
        midpointLine(b, d, b, e)
        midpointLine(a, e, b, e)
    if inputs == "9":
        midpointLine(a, c, b, c)
        midpointLine(a, d, a, e) 
        midpointLine(b, c, b, d) 
        midpointLine(a, d, b, d)
        midpointLine(b, d, b, e)
        midpointLine(a, e, b, e)

def draw_points(a, b):
    glPointSize(4) #pixel size. by default 1 thake
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
    glColor3f(0.0, 1.0, 0.0) #konokichur color set (RGB)
    a = 70
    b= a+150
    c=100
    d=250
    e=400
    letters(inputs[-2], a=a, b=b, c=c, d=d, e=e)
    a = b + 40 
    b = a + 150
    letters(inputs[-1], a=a, b=b, c=c, d=d, e=e)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
inputs=input("Write your Student ID:")
wind = glutCreateWindow(f"Student ID: {inputs}. Let's draw: {inputs[-2]}{inputs[-1]}") #window name
glutDisplayFunc(showScreen)
glutMainLoop()
