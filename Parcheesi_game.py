from graphics import *
from random import randrange
from pdb import *

# dieview.py
from graphics import *


class DieView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win  # save this for drawing pips later
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size  # radius of each pip
        hsize = size / 2.0  # half the size of the die
        offset = 0.6 * hsize  # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx - offset, cy - offset)
        self.pip2 = self.__makePip(cx - offset, cy)
        self.pip3 = self.__makePip(cx - offset, cy + offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx + offset, cy - offset)
        self.pip6 = self.__makePip(cx + offset, cy)
        self.pip7 = self.__makePip(cx + offset, cy + offset)

        # Draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set this die to display value."
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)


class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False



class Design:
    def __init__(self, win, center, width, height,):
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('paleturquoise')
        self.rect.draw(win)


    def blue(self, win):
        self.blue_nest = Rectangle(Point(350, 60), Point(550, 260))
        self.blue_nest.setFill("light blue")
        self.blue_nest.draw(win)

        self.blue_circle = Circle(Point(450, 160), 100)
        self.blue_circle.setFill("blue")
        self.blue_circle.draw(win)

        self.blue_arrow = Polygon(Point(550, 260), Point(750, 260), Point(650, 360))
        self.blue_arrow.setFill("blue")
        self.blue_arrow.draw(win)

        self.blue_path = Rectangle(Point(550, 60), Point(616.6, 85))
        self.blue_path_clone = self.blue_path
        for i in range(1, 8):
            self.blue_path_clone =self.blue_path_clone.clone()
            self.blue_path_clone.draw(win)
            self.blue_path_clone.move(0, 25)

        self.blue_path2 = Rectangle(Point(616.6, 60), Point(683.2, 85))
        self.blue_path2.draw(win)
        self.blue_path_clone2 = self.blue_path2
        for i in range(1, 8):
            self.blue_path_clone2 = self.blue_path_clone2.clone()
            self.blue_path_clone2.draw(win)
            self.blue_path_clone2.setFill("blue")
            self.blue_path_clone2.move(0, 25)

        self.blue_path3 = Rectangle(Point(683.2, 60), Point(749.8, 85))
        self.blue_path3.draw(win)
        self.blue_path_clone3 = self.blue_path3
        for i in range(1, 8):
            self.blue_path_clone3 = self.blue_path_clone3.clone()
            self.blue_path_clone3.draw(win)
            self.blue_path_clone3.move(0, 25)

        self.blue_start = Rectangle(Point(550, 160), Point(616.6, 185))
        self.blue_start.setFill("blue")
        self.blue_start.draw(win)

        self.blue_c1 = Circle(Point(583.3, 172.5), 10)
        self.blue_c1.draw(win)

        self.blue_c2 = Circle(Point(649.9, 72.5), 10)
        self.blue_c2.draw(win)

        self.blue_c3 = Circle(Point(716.5, 172.5), 10)
        self.blue_c3.draw(win)


    def red(self,win):
        self.red_nest = Rectangle(Point(750, 60), Point(950, 260))
        self.red_nest.setFill("pink")
        self.red_nest.draw(win)

        self.red_circle = Circle(Point(850, 160), 100)
        self.red_circle.setFill("red")
        self.red_circle.draw(win)

        self.red_arrow = Polygon(Point(750, 260), Point(750, 460), Point(650, 360))
        self.red_arrow.setFill("red")
        self.red_arrow.draw(win)

        self.red_p = Rectangle(Point(950, 460), Point(925, 393.4))
        self.red_p.draw(win)
        self.red_clone = self.red_p
        for i in range(1, 8):
            self.red_clone = self.red_clone.clone()
            self.red_clone.draw(win)
            self.red_clone.move(-25, 0)

        self.red_p2 = Rectangle(Point(950, 393.4), Point(925, 326.8))
        self.red_p2.draw(win)
        self.red_clone2 = self.red_p2
        for i in range(1, 8):
            self.red_clone2 = self.red_clone2.clone()
            self.red_clone2.setFill("red")
            self.red_clone2.draw(win)
            self.red_clone2.move(-25, 0)

        self.red_p3 = Rectangle(Point(950, 326.8), Point(925, 260.2))
        self.red_p3.draw(win)
        self.red_clone3 = self.red_p3
        for i in range(1, 8):
            self.red_clone3 = self.red_clone3.clone()
            self.red_clone3.draw(win)
            self.red_clone3.move(-25, 0)

        self.red_c = Circle(Point(937.5, 360.1), 10)
        self.red_c.draw(win)

        self.red_start = Rectangle(Point(850, 326.8), Point(825, 260.2))
        self.red_start.setFill("red")
        self.red_start.draw(win)

        self.red_c2 = Circle(Point(837.5, 293.5), 10)
        self.red_c2.draw(win)

        self.red_c3 = Circle(Point(837.5, 426.7), 10)
        self.red_c3.draw(win)


    def yellow(self, win):
        self.yellow_nest = Rectangle(Point(350, 460), Point(550, 660))
        self.yellow_nest.setFill("khaki")
        self.yellow_nest.draw(win)

        self.yellow_circle = Circle(Point(450, 560), 100)
        self.yellow_circle.setFill("yellow")
        self.yellow_circle.draw(win)

        self.yellow_arrow = Polygon(Point(550, 260), Point(550, 460), Point(650, 360))
        self.yellow_arrow.setFill("yellow")
        self.yellow_arrow.draw(win)

        self.yellow_p = Rectangle(Point(350, 260), Point(375, 326.6))
        self.yellow_p.draw(win)
        self.yellow_clone = self.yellow_p
        for i in range(1, 8):
            self.yellow_clone = self.yellow_clone.clone()
            self.yellow_clone.draw(win)
            self.yellow_clone.move(25, 0)

        self.yellow_p2 = Rectangle(Point(350, 326.6), Point(375, 393.2))
        self.yellow_p2.draw(win)
        self.yellow_clone2 = self.yellow_p2
        for i in range(1, 8):
            self.yellow_clone2 = self.yellow_clone2.clone()
            self.yellow_clone2.draw(win)
            self.yellow_clone2.setFill("yellow")
            self.yellow_clone2.move(25, 0)

        self.yellow_p3 = Rectangle(Point(350, 393.2), Point(375, 459.8))
        self.yellow_p3.draw(win)
        self.yellow_clone3 = self.yellow_p3
        for i in range(1, 8):
            self.yellow_clone3 = self.yellow_clone3.clone()
            self.yellow_clone3.draw(win)
            self.yellow_clone3.move(25, 0)

        self.yellow_start = Rectangle(Point(450, 393.2), Point(475, 459.8))
        self.yellow_start.setFill("yellow")
        self.yellow_start.draw(win)

        self.yellow_c1 = Circle(Point(462.5, 426.5), 10)
        self.yellow_c1.draw(win)

        self.yellow_c2 = Circle(Point(362.5, 359.9), 10)
        self.yellow_c2.draw(win)

        self.yellow_c3 = Circle(Point(462.5, 293.3), 10)
        self.yellow_c3.draw(win)



    def green(self, win):
        self.green_nest = Rectangle(Point(750, 460), Point(950, 660))
        self.green_nest.setFill("yellowgreen")
        self.green_nest.draw(win)

        self.green_circle = Circle(Point(850, 560), 100)
        self.green_circle.setFill("green")
        self.green_circle.draw(win)

        self.green_arrow = Polygon(Point(550, 460), Point(750, 460), Point(650, 360))
        self.green_arrow.setFill("green")
        self.green_arrow.draw(win)

        self.green_p = Rectangle(Point(550, 460), Point(616.6, 485))
        self.green_p.draw(win)
        self.green_clone = self.green_p
        for i in range(1, 8):
            self.green_clone = self.green_clone.clone()
            self.green_clone.draw(win)
            self.green_clone.move(0, 25)

        self.green_p2 = Rectangle(Point(616.6, 660), Point(683.2, 635))
        self.green_p2.draw(win)
        self.green_clone2 = self.green_p2
        for i in range(1, 8):
            self.green_clone2 = self.green_clone2.clone()
            self.green_clone2.draw(win)
            self.green_clone2.setFill("green")
            self.green_clone2.move(0, -25)

        self.green_p3 = Rectangle(Point(683.2, 660), Point(749.8, 635))
        self.green_p3.draw(win)
        self.green_clone3 = self.green_p3
        for i in range(1, 8):
            self.green_clone3 = self.green_clone3.clone()
            self.green_clone3.draw(win)
            self.green_clone3.move(0, -25)

        self.green_start = Rectangle(Point(683.2, 560), Point(749.8, 535))
        self.green_start.setFill("green")
        self.green_start.draw(win)

        self.green_c1 = Circle(Point(583.3, 547.5), 10)
        self.green_c1.draw(win)

        self.green_c2 = Circle(Point(649.9, 647.5), 10)
        self.green_c2.draw(win)

        self.green_c3 = Circle(Point(716.5, 547.5), 10)
        self.green_c3.draw(win)

    def homeNest(self, win):
        self.home = Rectangle(Point(550, 260), Point(750, 460))
        self.home.draw(win)



def main():
    win = GraphWin("Parcheesi Board Game", 1000, 700)
    win.setBackground("orange")

    board = Design(win, Point(650,360), 600, 600)
    board.blue(win)
    board.yellow(win)
    board.green(win)
    board.red(win)
    board.homeNest(win)


    die1 = DieView(win, Point(82.5, 165), 100)
    die2 = DieView(win, Point(82.5, 300), 100)

    roll_button = Button(win, Point(80, 75), 70, 50, "Roll Dice")
    roll_button.activate()

    quit_button = Button(win, Point(80, 575), 70, 50, "Quit")

    pt = win.getMouse()
    while not quit_button.clicked(pt):

            while roll_button.clicked(pt):
                value1 = randrange(1,7)
                die1.setValue(value1)
                value2 = randrange(1, 7)
                die2.setValue(value2)
                blue_piece = Circle(Point(460, 160), 6)
                blue_piece.setFill("light blue")
                blue_piece.draw(win)
                if value1 == 5 or value2 == 5:
                    if value1 != 5:
                            for i in range(value1):
                                if value1 < 4:
                                    blue_piece.undraw()
                                    blue_piece.move(110, 25)
                                    blue_piece.draw(win)
                                else:
                                    blue_piece.undraw()
                                    blue_piece.move(-12.5, 25/value1)
                                    blue_piece.draw(win)
                    elif value2 != 5:
                            for i in range(value2):
                                if value1 < 4:
                                    blue_piece.undraw()
                                    blue_piece.move(110, 25)
                                    blue_piece.draw(win)
                                else:
                                    blue_piece.undraw()
                                    blue_piece.move(-12.5, 25/value2)
                                    blue_piece.draw(win)

                    else:
                            blue_piece.undraw()
                            blue_piece.move(-12.5, 25 / value1)
                            blue_piece.draw(win)
                else:
                    pt = win.getMouse()
                quit_button.activate()

        # close up shop

main()
