from graphics import *

import random


class Tree:
    
    images_names = ['0_tree.png','1_little_burn.png','2_lot_burn.png','3_charcoal.png']
    
    def __init__(self,  x,   y):
        self.__x = x
        self.__y = y
        self.state = 0
        self.__image = Image(Point(15 + x * 30, 15 + y * 30), "0_tree.png")
        self.__exposed = False

    def set_exposed(self, new):
        self.__exposed = new

    def get_exposure(self):
        return self.__exposed

    def get_centre(self):
        return self.centre

    def get_state(self):
        return self.state

    def drawTree(self, win):
        self.__image.draw(win)

    def burn(self):
        if self.__state == 0:
            self.__image = Image(Point(15 + x * 30), (15 + y * 30), "1_little_burn.png")
            self.__image.draw(win)
##            if self.__y - 1 >= 0:
##                forest(self.__y - 1)
            self.__state += 1

        elif self.__state == 1:
            self.__image = Image(Point(15 + x * 30), (15 + y * 30), "2_lot_burn.png")
            self.__image.draw(win)
            self.__state += 1

        elif self.__state == 2:
            self.__image = Image(Point(15 + x * 30), (15 + y * 30), "3_charcoal.png")
            self.__image.draw(win)
            self.__state += 1

    def __str__(self):
        return "(" + str(x)+ ", " + str(y) + ")"

class Forest:
    def __init__(self):
        self.__forest = []
        
        for row in range(10):
            l_row = []
            for col in range(15):
                l_row.append(Tree(col, row))
            self.__forest.append(l_row)

    def draw_forest(self, win):
        for y in range(len(self.__forest)):
            for x in range(len(self.__forest[y])):
                self.__forest[y][x].drawTree(win)

    def get_forest(self):
        return self.__forest
    
    def burn_forest(self, prob):
    
        #self.__forest[0][0].burn()
        for y in range(len(self.__forest)):
            for x in range(len(self.__forest[y])):
                prob = random.random()
                if self.__forest[y][x].get_state() == 1 or self.__forest[y][x].get_state() == 2:
                    self.__forest[y][x].burn()

                        
    def compute(self, win):
       text = Text(Point(560, 120), "Burn Probability:")
       button = Rectangle(Point(465, 130), Point(655, 150))
       button.setFill("grey")
       button.setOutline("green")
       button.draw(win)
       text.draw(win)

    def exit_button(self, win):
        button = Rectangle(Point(670, 0), Point(700, 30))
        button.setFill("red")
        button.setOutline("black")
        center = button.getCenter()
        text = Text(center, "X")
        text.setTextColor("green")
        button.draw(win)
        text.draw(win)


    def random_button(self, win):
        button = Rectangle(Point(465, 160), Point(655, 180))
        button.setFill("orange")
        button.setOutline("black")
        center = button.getCenter()
        text = Text(center, "click for random start")
        button.draw(win)
        text.draw(win)

    def reset_button(self, win):
        button = Rectangle(Point(465, 195), Point(655, 215))
        center = button.getCenter()
        text = Text(center, "Click to reset")
        button.setFill("red")
        button.draw(win)
        text.draw(win)

   

def main():
    forest = Forest()
    win = GraphWin("myforest", 700, 300, autoflush = False)
    forest.draw_forest(win)

    forest.get_forest()

    forest.random_button(win)
    forest.reset_button(win)
    forest.compute(win)
    forest.exit_button(win)
    
    def getClick(win):
        click = win.getMouse()
        return click

    def clickCoords(click):
        xcoord = click.getX()
        ycoord = click.getY()
        return xcoord, ycoord

    def exitcoord(x, y):
        if x >= 670 and y <= 30:
            b_bool = True
        else:
            b_bool = False
        return b_bool

    click = getClick(win)
    xcoord, ycoord = clickCoords(click)
    b_bool = exitcoord(xcoord, ycoord)

    while not b_bool:
        click = getClick(win)
        xcoord, ycoord = clickCoords(click)
        b_bool = exitcoord(xcoord, ycoord)

    if b_bool:
        win.close()

    
if __name__ == "__main__":
    main()
