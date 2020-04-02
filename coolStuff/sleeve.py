import matplotlib as mpl
import matplotlib.pyplot as plt

from coolStuff.fts import getFTS
from coolStuff.limitCycle import getLimitCycle
from defines import Params, Model, sqrt, sq, Point, transformPointList
from modelling.stochasticClouds import mod_system_with_noise

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

def getSleeve(params: Params, noise: float):
    q = 1.386  # 0.95

    limitCycle = getLimitCycle(params)
    result1, result2 = [], []
    for cyclePoint, fts in zip(limitCycle, getFTS(params, limitCycle)):
        normalPoint = Model.getSystemPointNormalized(cyclePoint, params)
        multiplier = q * noise * sqrt(2 * fts.y)
        shiftX, shiftY = multiplier * normalPoint.x * cyclePoint.x, multiplier * normalPoint.y * cyclePoint.y
        result1.append(Point(cyclePoint.x + shiftX, cyclePoint.y + shiftY))
        result2.append(Point(cyclePoint.x - shiftX, cyclePoint.y - shiftY))
    x, y = transformPointList(result1)
    plt.plot(x, y, color = 'red', alpha = 0.7)
    x, y = transformPointList(result2)
    plt.plot(x, y, color = 'red', alpha = 0.7)

if __name__ == '__main__':
    params = Params(0.001, 0.02, 0.6)
    noise = 0.03
    getSleeve(params, noise)
    mod_system_with_noise(params, noise, 'blue', 100000)
    plt.show()
