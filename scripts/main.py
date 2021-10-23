import numpy as np
from scripts.plotter.Curves import Curve
from scripts.plotter.Plotter import Plotter


if __name__ == "__main__":

    def convert_(fld):
        temp = eval(fld)
        return complex(temp[0], temp[1])

    zero = [0,0,0,0]
    zero[0], zero[1], zero[2], zero[3] = np.loadtxt(
        "../data/iterations.txt",
        dtype=np.complex_,
        unpack=True,
        converters={0: convert_, 1: convert_, 2: convert_, 3: convert_}
    )

    curves = [Curve(zero[i].tolist(), Curve.Type.DISCONNECTED) for i in range(4)]

    pt = Plotter()
    for curve in curves:
        pt.plot_curve(curve, (255, 0, 0))

    # noinspection PyUnresolvedReferences
    # .tolist() might return object, but we definitely supply a list, so it will work
    zeros = [(zero[i].tolist())[-1] for i in range(4)]
    pt.plot_points(zeros, (255, 255, 0), "circle")

    pt.wait()