"""
Adrien Trainor
CSC 170
Lab 17: Zelle Graphics
Lab Partner: Gabriel

Desc: Allows the user to draw a triangle using a Polygon and mouse clicks.
"""

from graphics import * # imports all Graphics commands
from Lab13Refactoring import *

## 3 clicks, 3 points
## draw lines between points to create triangle
## fill in triangle with color
## report the triangle's area
## create an exit button that closes the graphics window



## CREATE A SEPARATE MODULE FOR BAR GRAPH

def getClick(win):              # click
    click = win.getMouse()
    return click

def clickCoords(click):         # returns the coords of given click
    xcoord = click.getX()
    ycoord = click.getY()
    return xcoord, ycoord

def drawPoint(win, click):      # draws single point
    dot = Circle(click, 1)
    dot.draw(win)

def pointConvert(lst, index):   # converts coords into Point object
    """
    Takes a 2D list and the index of the desired coordinates.
    Converts the coordinates into a point object, returns point object.
    """
    coords = lst[index]
    xcoord = coords[0]
    ycoord = coords[1]
    pointObject = Point(xcoord, ycoord)
    return pointObject

def exempt(win):                # defines where the user cannot click
    point1 = Point(0, 330)
    point2 = Point(400, 330)
    exemptLine = Line(point1, point2)
    textPoint = Point(40, 365)
    exemptLine.draw(win)
    text = Text(textPoint, "Area: ")
    text.draw(win)

def pointValid(click, win):
    xcoord, ycoord = clickCoords(click)
    while ycoord >= 330:
        click = getClick(win)
        xcoord, ycoord = clickCoords(click)
    return click

def sideLength(x1, y1, x2, y2):     # gets length for 1 side    
    length = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    return length

def getLengths(lst):                # get lengths for all sides
    p1 = lst[0]         
    p2 = lst[1]                     # x = p[0], y = p[1]
    p3 = lst[2]
    side1 = sideLength(p1[0], p1[1], p2[0], p2[1])
    side2 = sideLength(p2[0], p2[1], p3[0], p3[1])
    side3 = sideLength(p3[0], p3[1], p1[0], p1[1])
    return side1, side2, side3

def drawTri(win):
    # for 3 times:
    # get click
    # draw click (point)
    # get coords of click
    # draw line between coords
    points = 0
    triCoords = []
    while points < 3:           # draws 3 points + stores their coords
        click = getClick(win)
        click = pointValid(click, win)
        drawPoint(win, click)
        xcoord, ycoord = clickCoords(click)
        l_coords = [xcoord, ycoord]
        triCoords.append(l_coords)
        points += 1
    point1 = pointConvert(triCoords, 0)
    point2 = pointConvert(triCoords, 1)
    point3 = pointConvert(triCoords, 2)
    triangle = Polygon(point1, point2, point3)
    
    triangle.setFill("cyan")
    triangle.draw(win)
    return triCoords
def printArea(win, area):       ## UNFINISHED
    areaString = "x"
    textPoint = Point(117, 365)
    areaText = Text(textPoint, areaString)
    areaText.draw(win)

def exitcoord(x, y):
    if (x < 290) or (x > 390):
        b_x = False
    elif x >= 290 and x <= 390:
        b_x = True
    if y < 340 or y > 390:
        b_y = False
    elif y >= 340 and y <= 390:
        b_y = True
    return b_x, b_y

def exitbutton(win):
    p1 = Point(290, 340)
    p2 = Point(390, 340)
    p3 = Point(290, 390)
    p4 = Point(390, 390)
    button = Polygon(p1, p2, p4, p3, p1)
    button.setFill(color_rgb(238, 47, 47))
    centre = Point(340, 365)
    text = Text(centre, "EXIT")
    text.setStyle("bold")
    button.draw(win)
    text.draw(win)

    click = getClick(win)
    xcoord, ycoord = clickCoords(click)
    b_x, b_y = exitcoord(xcoord, ycoord)

    while not (b_x or b_y):
        click = getClick(win)
        xcoord, ycoord = clickCoords(click)
        b_x, b_y = exitcoord(xcoord, ycoord)
        
    if b_x and b_y:
        win.close()



def main():
    win = GraphWin("Triangle Time", 400, 400)
    exempt(win)
    

    triangle = drawTri(win)
    x = [triangle[0][0], triangle[1][0], triangle[2][0]]
    y = [triangle[0][1], triangle[1][1], triangle[2][1]]
    area = triangle_area(distance(x, y))
    printArea(win, area)
    exitbutton(win)
    
    win.getMouse() # EXIT (REMOVE LATER)
    win.close()

main()
