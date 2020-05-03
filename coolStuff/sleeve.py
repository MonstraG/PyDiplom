import matplotlib as mpl
import matplotlib.pyplot as plt

from coolStuff.fts import getFTS
from coolStuff.limitCycle import getLimitCycle
from defines import Params, Model, rt, Point, transformPointList, RK

mpl.rcParams['figure.dpi'] = 140
plt.grid(True)

def getSleeve(params: Params, noise: float, reshuffleCycle: bool = False):
    q = 1.821  # 0.99

    limitCycle = getLimitCycle(params)
    result1, result2 = [], []
    for cyclePoint, fts in zip(limitCycle, getFTS(params, limitCycle, reshuffleCycle)):
        normalPoint = Model.getSystemPointNormalized(cyclePoint, params)
        multiplier = q * noise * rt(2 * fts.y)
        shiftX, shiftY = multiplier * normalPoint.x * cyclePoint.x, multiplier * normalPoint.y * cyclePoint.y
        result1.append(Point(cyclePoint.x + shiftX, cyclePoint.y + shiftY))
        result2.append(Point(cyclePoint.x - shiftX, cyclePoint.y - shiftY))
    x, y = transformPointList(result1)
    plt.plot(x, y, color = 'red', alpha = 0.7)
    x, y = transformPointList(result2)
    plt.plot(x, y, color = 'red', alpha = 0.7)

def sleevePlot(params: Params, noise: float, reshuffleCycle: bool):
    getSleeve(params, noise, reshuffleCycle)

    current = Point(4, 0.1)
    values_x, values_y = [current.x], [current.y]
    for _ in range(500000):
        current = RK.getNewPointWithNoise(current, params, noise)
        values_x.append(current.x)
        values_y.append(current.y)
    return values_x, values_y

if __name__ == '__main__':
    params = Params.defaultWithCycle()
    noise = 0.03
    reshuffleCycle = True
    values_x, values_y = sleevePlot(params, noise, reshuffleCycle)
    plt.plot(values_x[10000:], values_y[10000:], color = 'blue', alpha = 0.5, linewidth=0.5)
    plt.title(f'Sleeve, {params}, noise: {noise}, cycle: {"normal" if not reshuffleCycle else "reshuffled"}')
    plt.show()
