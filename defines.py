import numpy as np
from typing import List

def toStr(num: float) -> str:
    return str(float(f'{num:.4f}'))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Point({self.x}, {self.y})'

def transformPointList(points: List[Point]) -> (List[float], List[float]):
    return [p.x for p in points], [p.y for p in points]

class Params:
    def __init__(self, step: float, a: float, b: float):
        self.step = step
        self.a = a
        self.b = b

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Params(step: {toStr(self.step)}, a:{toStr(self.a)}, b:{toStr(self.b)})'

    @staticmethod
    def defaultWithCycle():
        return Params(0.001, 0.02, 0.6)

rt = lambda x: x ** .5
sq = lambda x: x ** 2
noiseShift = lambda: np.random.normal(size = 2).tolist()

class Model:
    aPlusBSq = staticmethod(lambda p: p.a + sq(p.b))
    getStationaryPoint = staticmethod(lambda p: Point(p.b, p.b / Model.aPlusBSq(p)))

    getU = staticmethod(lambda p: 2 * sq(p.b) / Model.aPlusBSq(p))
    getV = staticmethod(lambda p: Model.aPlusBSq(p))
    getFx = staticmethod(lambda p: Model.getU(p) - 1)
    getFy = staticmethod(lambda p: Model.getV(p))
    getGx = staticmethod(lambda p: -Model.getU(p))
    getGy = staticmethod(lambda p: -Model.getV(p))
    getDifferentials = staticmethod(lambda p: (Model.getFx(p), Model.getFy(p), Model.getGx(p), Model.getGy(p)))

    getF = staticmethod(lambda p, params: -p.x + params.a * p.y + sq(p.x) * p.y)
    getG = staticmethod(lambda p, params: params.b - params.a * p.y - sq(p.x) * p.y)
    getSystemPoint = staticmethod(lambda p, params: (Model.getF(p, params), Model.getG(p, params)))

    @staticmethod
    def getSystemPointNormalized(p: Point, params: Params) -> Point:
        f, g = Model.getF(p, params), Model.getG(p, params)
        divisor = rt(sq(f) + sq(g))
        return Point(-g / divisor, f / divisor)

class RK:
    @staticmethod
    def getNewPointWithNoise(prev: Point, params: Params, noise: float) -> Point:
        newPoint = RK.getNewPoint(prev, params)
        noise_x, noise_y = noiseShift()
        return Point(
            newPoint.x + noise * rt(params.step) * noise_x * prev.x,
            newPoint.y + noise * rt(params.step) * noise_y * prev.y
        )

    @staticmethod
    def __f(prev: Point, params: Params, k: float, l: float) -> float:
        modifiedPrev = Point(prev.x + k / 2, prev.y + l / 2)
        return Model.getF(modifiedPrev, params)

    @staticmethod
    def __g(prev: Point, params: Params, k: float, l: float) -> float:
        modifiedPrev = Point(prev.x + k / 2, prev.y + l / 2)
        return Model.getG(modifiedPrev, params)

    @staticmethod
    def getNewPoint(prev: Point, params: Params) -> Point:
        K1 = params.step * RK.__f(prev, params, 0.0, 0.0)
        L1 = params.step * RK.__g(prev, params, 0.0, 0.0)
        K2 = params.step * RK.__f(prev, params, K1 / 2, L1 / 2)
        L2 = params.step * RK.__g(prev, params, K1 / 2, L1 / 2)
        K3 = params.step * RK.__f(prev, params, K2 / 2, L2 / 2)
        L3 = params.step * RK.__g(prev, params, K2 / 2, L2 / 2)
        K4 = params.step * RK.__f(prev, params, K3, L3)
        L4 = params.step * RK.__g(prev, params, K3, L3)
        return Point(
            prev.x + 1.0 / 6.0 * (K1 + 2 * K2 + 2 * K3 + K4),
            prev.y + 1.0 / 6.0 * (L1 + 2 * L2 + 2 * L3 + L4)
        )

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]