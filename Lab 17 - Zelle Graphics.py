from graphics import *

win = GraphWin("Draw Triangle", 400, 400)


##circ_center = win.getMouse()
##circ = Circle(circ_center, 50)
##xcoord = circ_center.getX()
##ycoord = circ_center.getY()
##text = Text(circ_center, f'({xcoord}, {ycoord})')
##circ.draw(win)
##text.draw(win)
##win.getMouse() # wait for click to exit
##win.close()    # close the window when the program is about to end


##def Click(win):
##  return point
##
##def GetCoords():
##    x_coord_1 = point.get
##
##def Clickcoords
##
##def PointConvert()
##
##def Exempt(win):
##   
##
##def DrawTri


point_4 = Point(0, 325)
point_5 = Point(400, 325)


aline = Polygon(point_4, point_5)
aline.draw(win)

textpoint = Point(40, 360)
text = Text(textpoint, "Area:")
text.draw(win)

point = win.getMouse()
circ_point_1 = Circle(point, 0.75)
x_coord_1 = point.getX()
y_coord_1 = point.getY()
circ_point_1.draw(win)

point = win.getMouse()
circ_point_2 = Circle(point, 0.75)
x_coord_2 = point.getX()
y_coord_2 = point.getY()
circ_point_2.draw(win)

point = win.getMouse()
circ_point_3 = Circle(point, 0.75)
x_coord_3 = point.getX()
y_coord_3 = point.getY()
circ_point_3.draw(win)


point_1 = Point(x_coord_1, y_coord_1)
point_2 = Point(x_coord_2, y_coord_2)
point_3 = Point(x_coord_3, y_coord_3)

tri_polygon = Polygon(point_1, point_2, point_3)
tri_polygon.draw(win)
tri_polygon.setFill("Magenta")

##message =

