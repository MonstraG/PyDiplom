import matplotlib as mpl
import matplotlib.pyplot as plt

from coolStuff.fts import getFTS
from coolStuff.limitCycle import getLimitCycle
from defines import Params, Model, rt, Point, unzip, RK

mpl.rcParams['figure.dpi'] = 140
plt.grid(True)

def getSleeve(params: Params, noise: float, reshuffleCycle: bool = False):
    q = 1.821  # 0.99 With Applications to Physics, Biology, Chemistry, and Engineering

    limitCycle = getLimitCycle(params)
    result1, result2 = [], []
    for cyclePoint, fts in zip(limitCycle, getFTS(params, limitCycle, reshuffleCycle)):
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

def sleevePlot(params: Params, noise: float, reshuffleCycle: bool):
    getSleeve(params, noise, reshuffleCycle)
    return [x for x in RK.genPointNoise(params, noise, 500000, Point(4, 0.1))]

if __name__ == '__main__':
    params = Params.defaultWithCycle()
    noise = 0.03
    reshuffleCycle = True
    values_x, values_y = unzip(sleevePlot(params, noise, reshuffleCycle))
    plt.plot(values_x[10000:], values_y[10000:], color = 'blue', alpha = 0.5, linewidth = 0.5)
    plt.title(f'Sleeve, {params}, noise: {noise}, cycle: {"normal" if not reshuffleCycle else "reshuffled"}')
    plt.show()
