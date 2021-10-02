from typing import Tuple, List
from graphics import *

from linesdrawer import LinesDrawer
from Curves import Curve

defaultDimensions = [1000, 800]
defaultScale = [50.0, 50.0]
defaultOffset = [0.0, 0.0]


class Plotter:

    def __init__(self, dimensions=None, scale=None, offset=None, draw_axis=LinesDrawer.Type.STANDARD,
                 name="ComplexPlotter"):
        self.drawAxisType = draw_axis
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

        self.origin = [self.dimensions[0] / 2 + self.offset[0] * self.scale[0],
                       self.dimensions[1] / 2 + self.offset[1] * self.scale[1]]
        self.win = GraphWin(name, self.dimensions[0], self.dimensions[1])
        self.win.setBackground(color_rgb(0, 0, 0))
        LinesDrawer.drawAxies(self.win, self.drawAxisType, self.scale, self.origin)

    def _complex2point(self, a: complex) -> tuple:
        return a.real * self.scale[0] + self.origin[0], a.imag * self.scale[1] + self.origin[1]

    def plot_point(self, input: complex, color: Tuple[int, int, int], type="default", width=3) -> None:
        color = color_rgb(*color)
        x, y = self._complex2point(input)
        if type == "default":
            self.win.plot(x, y, color)
        else:
            if type == "circle":
                obj = Circle(Point(x, y), width)
            else:  # type == "square":
                obj = Rectangle(
                    Point(x - width, y - width),
                    Point(x + width, y + width)
                )
            obj.setFill(color)
            obj.setOutline(color)
            obj.draw(self.win)

    def plot_points(self, input: List[complex], color: Tuple[int, int, int], type="default", width=3):
        for elem in input:
            self.plot_point(elem, color, type, width)

    def plot_line(self, input: Tuple[complex, complex], color) -> None:
        x1, y1 = self._complex2point(input[0]);
        x2, y2 = self._complex2point(input[1])
        obj = Line(Point(x1, y1), Point(x2, y2))

        color = color_rgb(*color)
        obj.setFill(color)
        obj.draw(self.win)

    def plot_curve(self, a: Curve, color):
        if a.type == Curve.Type.DEFAULT:
            self.plot_points(a.points, color)
        else:
            for index in range(len(a.points) - 1):
                self.plot_line((a.points[index], a.points[index + 1]), color)
            if a.type == Curve.Type.CLOSED_LOOP:
                self.plot_line((a.points[0], a.points[-1]), color)

    def clear(self):
        self.win.delete("all")
        LinesDrawer.drawAxies(self.win, self.drawAxisType, self.scale, self.origin)

    def wait(self):
        self.win.getMouse()


"""
Testing area
"""

import time

if __name__ == "__main__":
    plotter = Plotter(draw_axis=LinesDrawer.Type.NONE)
    plotter.plot_point(complex(1, 1), (255, 0, 0), "circle")
    ls = [complex(-1, i) for i in range(-1, 2)]
    plotter.plot_points(ls, (255, 0, 0))

    curve = Curve([complex(-2, -2), complex(-2, 2), complex(2, 0)], Curve.Type.CLOSED_LOOP)
    plotter.plot_curve(curve, (0, 255, 0))
    plotter.wait()


    def func(a: complex) -> complex:
        return a * complex(0, 1)


    curves = curve.transform_smoothly(func, 100)
    for i, elem in enumerate(curves):
        plotter.clear()
        plotter.plot_curve(elem, (0, 255, 0))
        time.sleep(0.01 * (i / 50 - 1) ** 2)

    plotter.wait()
