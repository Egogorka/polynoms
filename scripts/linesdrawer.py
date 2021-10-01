from graphics import *
from enum import Enum

class LinesDrawer:

    class Type(Enum):
        NONE = 0
        MINIMAL = 1
        NO_LINES = 2
        STANDARD = 3

    @staticmethod
    def drawAxies(win, type: Type, scale, origin, frequency=1):
        self = LinesDrawer

        if type == LinesDrawer.Type.NONE:
            return

        if type == LinesDrawer.Type.MINIMAL:
            self.drawAxiesMinimalistic(win, scale, origin, frequency)
            return

        if type == LinesDrawer.Type.NO_LINES:
            self.drawThingies(win, scale, origin, frequency)
            return

        #in other cases
        self.drawStandart(win, scale, origin, frequency)

    @staticmethod
    def drawStandart(win, scale, origin, frequency):
        self = LinesDrawer

        xAxis = Line(Point(0, origin[1]), Point(win.getWidth(), origin[1]))
        yAxis = Line(Point(origin[0], 0), Point(origin[0], win.getHeight()))

        xAxis.setFill("white")
        yAxis.setFill("white")

        xAxis.draw(win)
        yAxis.draw(win)
        self.drawThingies(win, scale, origin, frequency)

    @staticmethod
    def drawThingies(win, scale, origin, frequency=1):
        # Small dx or dy
        d = 3

        # drawing thingies on the right of oX
        # print(range(int(origin[0]), int(win.getWidth()), int(scale[0])))
        units_left = win.getWidth()

        for i in range(int(origin[0]) + int(scale[0]), int(win.getWidth()), frequency*int(scale[0])):
            l = Line(Point(i, origin[1] - d), Point(i, origin[1] + d))
            l.setFill("white")
            l.draw(win)

            t = Text(Point(i, origin[1] + d + 10), int((i - origin[0]) / scale[0]))
            t.setFill("white")
            t.draw(win)

        # drawing thingies on the left of oX
        for i in range(int(origin[0]) - int(scale[0]), 0, -frequency*int(scale[0])):
            l = Line(Point(i, origin[1] - d), Point(i, origin[1] + d))
            l.setFill("white")
            l.draw(win)

            t = Text(Point(i, origin[1] + d + 10), int((i - origin[0]) / scale[0]))
            t.setFill("white")
            t.draw(win)

        # drawing thingies on the down of oY
        for i in range(int(origin[1]) + int(scale[1]), win.getHeight(), frequency*int(scale[1])):
            l = Line(Point(origin[0] - d, i), Point(origin[0] + d, i))
            l.setFill("white")
            l.draw(win)

            t = Text(Point(origin[0] + d + 10, i), complex(0, int(-(i - origin[1]) / scale[0])))
            t.setFill("white")
            t.draw(win)

        # drawing thingies on the up of oY
        for i in range(int(origin[1]) - int(scale[1]), 0, -frequency*int(scale[1])):
            l = Line(Point(origin[0] - d, i), Point(origin[0] + d, i))
            l.setFill("white")
            l.draw(win)

            t = Text(
                Point(origin[0] + d + 10, i),
                complex(0, int(-(i - origin[1]) / scale[0])))
            t.setFill("white")
            t.draw(win)

    @staticmethod
    def drawAxiesMinimalistic(win, scale, origin, frequency=1):

        # drawing thingies on the right of oX
        for i in range(int(origin[0]) + int(scale[0]), int(win.getWidth()), frequency*int(scale[0])):
            win.plot(i, origin[1], "white")
        # drawing thingies on the left of oX
        for i in range(int(origin[0]) - int(scale[0]), 0, -frequency*int(scale[0])):
            win.plot(i, origin[1], "white")
        # drawing thingies on the down of oY
        for i in range(int(origin[1]) + int(scale[1]), win.getHeight(), frequency*int(scale[1])):
            win.plot(origin[0], i, "white")
        # drawing thingies on the up of oY
        for i in range(int(origin[1]) - int(scale[1]), 0, -frequency*int(scale[1])):
            win.plot(origin[0], i, "white")
