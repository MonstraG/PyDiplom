from typing import Generator, List, Union

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def unzip(points: Union[Generator[Point, None, None], List[Point]]):
    return zip(*[(p.x, p.y) for p in points])

class Params:
    def __init__(self, step: float, a: float, b: float):
        self.step = step
        self.a = a
        self.b = b

    @staticmethod
    def defaultWithCycle():
        return Params(0.001, 0.02, 0.6)

rt = lambda x: x ** .5
sq = lambda x: x ** 2
noiseShift = lambda: np.random.normal(size=1)

class Model:
    aPlusBSq = staticmethod(lambda p: p.a + sq(p.b))

    @staticmethod
    def stationaryPoint(p: Params):
        return Point(p.b, p.b / Model.aPlusBSq(p))

    y = staticmethod(lambda p: 2 * sq(p.b) / Model.aPlusBSq(p))
    v = staticmethod(lambda p: Model.aPlusBSq(p))
    fx = staticmethod(lambda p: Model.y(p) - 1)
    fy = staticmethod(lambda p: Model.v(p))
    gx = staticmethod(lambda p: -Model.y(p))
    gy = staticmethod(lambda p: -Model.v(p))

    @staticmethod
    def getDifferentials(p: Params):
        return Model.fx(p), Model.fy(p), Model.gx(p), Model.gy(p)

    f = staticmethod(lambda p, params: -p.x + params.a * p.y + sq(p.x) * p.y)
    g = staticmethod(lambda p, params: params.b - params.a * p.y - sq(p.x) * p.y)

    @staticmethod
    def getSystemPointNormalized(p: Point, params: Params) -> Point:
        f, g = Model.f(p, params), Model.g(p, params)
        divisor = rt(sq(f) + sq(g))
        return Point(-g / divisor, f / divisor)

class RK:
    @staticmethod
    def getNewPointWithNoise(prev: Point, params: Params, noise: float):
        new = RK.getNewPoint(prev, params)
        return Point(
            new.x + noise * rt(params.step) * noiseShift()[0] * prev.x,
            new.y + noise * rt(params.step) * noiseShift()[0] * prev.y
        )

    @staticmethod
    def _f(prev: Point, params: Params, k: float, l: float) -> float:
        modifiedPrev = Point(prev.x + k / 2, prev.y + l / 2)
        return Model.f(modifiedPrev, params)

    @staticmethod
    def _g(prev: Point, params: Params, k: float, l: float) -> float:
        modifiedPrev = Point(prev.x + k / 2, prev.y + l / 2)
        return Model.g(modifiedPrev, params)

    @staticmethod
    def getNewPoint(prev: Point, params: Params) -> Point:
        K1, L1 = (params.step * RK._f(prev, params, 0.0, 0.0),
                  params.step * RK._g(prev, params, 0.0, 0.0))
        K2, L2 = (params.step * RK._f(prev, params, K1 / 2, L1 / 2),
                  params.step * RK._g(prev, params, K1 / 2, L1 / 2))
        K3, L3 = (params.step * RK._f(prev, params, K2 / 2, L2 / 2),
                  params.step * RK._g(prev, params, K2 / 2, L2 / 2))
        K4, L4 = (params.step * RK._f(prev, params, K3, L3),
                  params.step * RK._g(prev, params, K3, L3))
        return Point(
            prev.x + 1.0 / 6.0 * (K1 + 2 * K2 + 2 * K3 + K4),
            prev.y + 1.0 / 6.0 * (L1 + 2 * L2 + 2 * L3 + L4)
        )

    @staticmethod
    def genPoint(params: Params, steps: int, start: Point):
        for _ in range(steps):
            yield start
            start = RK.getNewPoint(start, params)

    @staticmethod
    def genPointNoise(p: Params, noise: float, steps: int, st: Point = None):
        if st is None:
            st = Model.stationaryPoint(p)
        for _ in range(steps):
            yield st
            st = RK.getNewPointWithNoise(st, p, noise)
