from typing import Callable

from defines import *

getNewIntersect: Callable[[Point, Point], float] = lambda cr, nw, y0: \
    -((nw.x - cr.x) * y0 + (cr.x * nw.y - nw.x * cr.y)) / (cr.y - nw.y)

def getLimitCycle(model: Model):
    intersectEpsilon = 0.000001
    current = Point(4.0, 0.1)
    result = []
    stPoint = model.stationaryPoint
    x0, y0 = stPoint.x, stPoint.y
    curIntersect = float('Inf')
    while True:
        newPoint = RK.getNewPoint(model, current)
        if ((current.y - y0) * (newPoint.y - y0) < 0 and
                current.x > x0 and newPoint.x > x0):
            newIntersect = getNewIntersect(current, newPoint, y0)
            if abs(newIntersect - curIntersect) < intersectEpsilon:
                current = Point(newIntersect, y0)
                while not ((current.y - y0) * (newPoint.y - y0) < 0 and
                           current.x > x0 and newPoint.x > x0):
                    result.append(newPoint)
                    current = Point(newPoint.x, newPoint.y)
                    newPoint = RK.getNewPoint(model, current)
                result.append(newPoint)
                result.append(result[0])
                return result
            curIntersect = newIntersect
        current = Point(newPoint.x, newPoint.y)

if __name__ == '__main__':
    step = 0.001
    models = [
        Model(step, 0.005, 0.95),
        Model(step, 0.06, 0.85),
        Model(step, 0.1, 0.75),
        Model(step, 0.005, 0.6),
        Model(step, 0.06, 0.6),
        Model(step, 0.12, 0.6),
        Model(step, 0.005, 0.1),
        Model(step, 0.06, 0.35),
        Model(step, 0.1, 0.45)
    ]
    for i, model in enumerate(models):
        x, y = unzip(getLimitCycle(model))
        plt.subplot(3, 3, i + 1)
        plt.plot(x, y, color='blue', alpha=0.7)
        plt.grid(True)
    plt.show()
