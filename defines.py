from typing import Generator, List, Union

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def unzip(points: Union[Generator[Point, None, None], List[Point]]):
    return zip(*[(p.x, p.y) for p in points])

rt = lambda x: x ** .5
sq = lambda x: x ** 2
noiseShift = lambda: np.random.normal(size=1)

class Model:
    def __init__(self, step: float, a: float, b: float):
        self.step = step
        self.a = a
        self.b = b

    @staticmethod
    def defaultWithCycle(step: float = 0.001):
        return Model(step=step, a=0.02, b=0.6)

    aPlusBSq = property(lambda self: self.a + sq(self.b))

    @property
    def stationaryPoint(self) -> Point:
        return Point(self.b, self.b / self.aPlusBSq)

    y = property(lambda self: 2 * sq(self.b) / self.aPlusBSq)
    v = property(lambda self: self.aPlusBSq)
    fx = property(lambda self: self.y - 1)
    fy = property(lambda self: self.v)
    gx = property(lambda self: -self.y)
    gy = property(lambda self: -self.v)

    @property
    def differentials(self):
        return self.fx, self.fy, self.gx, self.gy

    f = lambda self, p: -p.x + self.a * p.y + sq(p.x) * p.y
    g = lambda self, p: self.b - self.a * p.y - sq(p.x) * p.y

    def getSystemPointNormalized(self, p: Point) -> Point:
        f, g = self.f(p), self.g(p)
        divisor = rt(sq(f) + sq(g))
        return Point(-g / divisor, f / divisor)

class RK:
    @staticmethod
    def _f(model: Model, prev: Point, k: float, l: float) -> float:
        return model.f(Point(prev.x + k / 2, prev.y + l / 2))

    @staticmethod
    def _g(model: Model, prev: Point, k: float, l: float) -> float:
        return model.g(Point(prev.x + k / 2, prev.y + l / 2))

    @staticmethod
    def getNewPoint(model: Model, prev: Point) -> Point:
        K1, L1 = (model.step * RK._f(model, prev, 0.0, 0.0),
                  model.step * RK._g(model, prev, 0.0, 0.0))
        K2, L2 = (model.step * RK._f(model, prev, K1 / 2, L1 / 2),
                  model.step * RK._g(model, prev, K1 / 2, L1 / 2))
        K3, L3 = (model.step * RK._f(model, prev, K2 / 2, L2 / 2),
                  model.step * RK._g(model, prev, K2 / 2, L2 / 2))
        K4, L4 = (model.step * RK._f(model, prev, K3, L3),
                  model.step * RK._g(model, prev, K3, L3))
        return Point(
            prev.x + (K1 + 2 * K2 + 2 * K3 + K4) / 6,
            prev.y + (L1 + 2 * L2 + 2 * L3 + L4) / 6
        )

    @staticmethod
    def getNewPointWithNoise(model: Model, prev: Point, noise: float):
        new = RK.getNewPoint(model, prev)
        return Point(
            new.x + noise * rt(model.step) * noiseShift()[0] * prev.x,
            new.y + noise * rt(model.step) * noiseShift()[0] * prev.y
        )

    @staticmethod
    def genPoint(model: Model, steps: int, current: Point):
        for _ in range(steps):
            yield current
            current = RK.getNewPoint(model, current)

    @staticmethod
    def genPointNoise(model: Model, steps: int, noise: float,
                      current: Point = None):
        if current is None:
            current = model.stationaryPoint
        for _ in range(steps):
            yield current
            current = RK.getNewPointWithNoise(model, current, noise)
