from graphics import *

defaultDimensions = [200, 200]
defaultScale = [10.0, 10.0]
defaultOffset = [0.0, 0.0]

class ComplexPlotter:

    def __init__(self, dimensions=None, scale=None, offset=None, draw_axies="None", name="ComplexPlotter"):
        self.drawAxiesType = draw_axies
        if scale is None:
            self.scale = defaultScale
        else:
            self.scale = scale

        if dimensions is None:
            self.dimensions = defaultDimensions
        else:
            self.dimensions = dimensions

        if offset is None:
            self.offset = defaultOffset
        else:
            self.offset = offset

        self.origin = [self.dimensions[0] / 2 + offset[0]*scale[0], self.dimensions[1] / 2 + offset[1]*scale[1]]
        self.win = GraphWin(name, self.dimensions[0], self.dimensions[1])
        self.win.setBackground(color_rgb(0,0,0))


    def clearScreen(self):
        self.win.delete("all")
        if self.drawAxiesType != "None" :
            LinesDrawer.drawAxies(self.win, self.drawAxiesType, self.dimensions, self.scale, self.origin)

    def plotPoint(self, complex, color, type="default", width=3):
        if type == "default":
            self.win.plot(complex.real*self.scale[0]+self.origin[0], complex.imag*self.scale[1]+self.origin[1], color)
        else:
            self.drawPoint(complex, color, width)

    def plotPoints(self, array, color, type="default", width=3):
        for elem in array:
            self.plotPoint(elem, color, type, width)

    def drawPoint(self, c, color, width=3):
        point = Circle(Point(c.real*self.scale[0]+self.origin[0], c.imag*self.scale[1]+self.origin[1]), width)
        point.setFill(color)
        point.setOutline(color)

        point.draw(self.win)
        return point

    def drawCircle(self, c, color, radius):
        pt1 = Point((c.real+radius)*self.scale[0]+self.origin[0], (c.imag+radius)*self.scale[1]+self.origin[1])
        pt2 = Point((c.real-radius)*self.scale[0]+self.origin[0], (c.imag-radius)*self.scale[1]+self.origin[1])

        circle = Oval(pt1,pt2)
        circle.setOutline(color)
        circle.draw(self.win)
        return circle

    def drawLine(self, c1, c2, color):
        p1x = c1.real*self.scale[0]+self.origin[0]
        p1y = c1.imag*self.scale[1]+self.origin[1]

        p2x = c2.real * self.scale[0] + self.origin[0]
        p2y = c2.imag * self.scale[1] + self.origin[1]

        line = Line(Point(p1x,p1y), Point(p2x, p2y))
        line.setFill(color)

        line.draw(self.win)
        return line

    def getPoint(self):
        pt = self.win.getMouse()
        z = complex( (pt.x - self.origin[0]) / self.scale[0], (pt.y - self.origin[1]) / self.scale[1])
        return z

    def bindMove(self, handler):
        def interim( event ):
            handler(complex( (event.x - self.origin[0]) / self.scale[0], (event.y - self.origin[1]) / self.scale[1]))
        self.win.bind('<Motion>', interim)

    def unbindMove(self):
        self.win.unbind('<Motion>')

    def wait(self):
            self.win.getMouse()