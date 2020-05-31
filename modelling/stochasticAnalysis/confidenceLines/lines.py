from typing import Generator

import matplotlib as mpl
import matplotlib.pyplot as plt

from modelling.stochasticAnalysis.SSF import getSSF
from modelling.stochasticAnalysis.limitCycle import getLimitCycle
from defines import Params, Model, rt, Point, unzip, RK

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

def getSleeve(params: Params, noise: float, reshuffleCycle: bool = False):
    q = 1.386  # 0.95, 1/erf(0.95)

    limitCycle = getLimitCycle(params)
    result1, result2 = [], []
    for cyclePoint, fts in zip(limitCycle, getSSF(params, limitCycle, reshuffleCycle)):
        normalPoint = Model.getSystemPointNormalized(cyclePoint, params)
        multiplier = q * noise * rt(2 * fts.y)
        shiftX, shiftY = (multiplier * normalPoint.x * cyclePoint.x,
                          multiplier * normalPoint.y * cyclePoint.y)
        result1.append(Point(cyclePoint.x + shiftX, cyclePoint.y + shiftY))
        result2.append(Point(cyclePoint.x - shiftX, cyclePoint.y - shiftY))
    x, y = unzip(result1)
    plt.plot(x, y, color = 'red', alpha = 0.7)
    x, y = unzip(result2)
    plt.plot(x, y, color = 'red', alpha = 0.7)

def sleevePlot(params: Params, noise: float, reshuffleCycle: bool = False, steps: int = 5000000) -> Generator[Point, None, None]:
    getSleeve(params, noise, reshuffleCycle)
    return RK.genPointNoise(params, noise, steps, Point(2, 0.1))

if __name__ == '__main__':
    params = Params.defaultWithCycle()
    noise = 0.02
    reshuffleCycle = False
    x, y = unzip(sleevePlot(params, noise, reshuffleCycle))
    plt.plot(x, y, color = 'blue', alpha = 0.5, linewidth = 0.5)
    plt.grid(True)
    plt.title(f'Доверительная полоса, {params}, шум: {noise}, {"цикл обращен" if reshuffleCycle else ""}')

    intersectEpsilon = 0.000001
    x, y = unzip(getLimitCycle(params, intersectEpsilon))
    plt.plot(x, y, color = 'green', alpha = 0.7)
    plt.show()
