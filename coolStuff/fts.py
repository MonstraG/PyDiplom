import math
import matplotlib.pyplot as plt

from coolStuff.limitCycle import getLimitCycle
from defines import Model, Params, Point, sq, transformPointList

def getFTS(params: Params, limitCycle: [] = None):
    cycle = getLimitCycle(params) if limitCycle is None else limitCycle
    r, h = [1.0], [0.0]
    fx, fy, gx, gy = Model.getDifferentials(params)
    for cyclePoint in cycle:
        p = Model.getSystemPointNormalized(cyclePoint, params)
        a = (p.x * (p.x * (gx + fy) + p.x * 2 * fx) +
             p.y * (p.y * (gx + fy) + p.y * 2 * gy))
        r.append(r[-1] * (math.e ** (a * params.step)))
        b = sq(p.x) * sq(cyclePoint.x) + sq(p.y) * sq(cyclePoint.y)
        h.append(h[-1] + b / r[-1] * params.step)

    c = r[-1] * h[-1] / (1 - r[-1])
    return [Point(i * params.step, rr * (c + hh)) for i, [rr, hh] in enumerate(zip(r, h))]

if __name__ == '__main__':
    params = Params.defaultWithCycle()
    points = getFTS(params)
    x, y = transformPointList(points)
    plt.plot(x, y, color = 'red', alpha = 0.7)

    plt.title(f'FTS, {params}')
    plt.grid(True)
    plt.show()