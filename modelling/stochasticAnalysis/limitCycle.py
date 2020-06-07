from typing import Callable

from defines import *

getNewIntersect: Callable[[Point, Point], float] = lambda cr, nw, y0: \
    -((nw.x - cr.x) * y0 + (cr.x * nw.y - nw.x * cr.y)) / (cr.y - nw.y)

def getLimitCycle(params: Params):
    intersectEpsilon = 0.000001
    current = Point(4.0, 0.1)
    result = []
    stPoint = Model.stationaryPoint(params)
    x0, y0 = stPoint.x, stPoint.y
    curIntersect = float('Inf')
    while True:
        newPoint = RK.getNewPoint(current, params)
        if ((current.y - y0) * (newPoint.y - y0) < 0 and
                current.x > x0 and newPoint.x > x0):
            newIntersect = getNewIntersect(current, newPoint, y0)
            if abs(newIntersect - curIntersect) < intersectEpsilon:
                current = Point(newIntersect, y0)
                while not ((current.y - y0) * (newPoint.y - y0) < 0 and
                           current.x > x0 and newPoint.x > x0):
                    result.append(newPoint)
                    current = Point(newPoint.x, newPoint.y)
                    newPoint = RK.getNewPoint(current, params)
                result.append(newPoint)
                result.append(result[0])
                return result
            curIntersect = newIntersect
        current = Point(newPoint.x, newPoint.y)

if __name__ == '__main__':
    paramExtremes = [
        Params(0.001, 0.005, 0.1),
        Params(0.001, 0.12, 0.6),
        Params(0.001, 0.005, 0.99)
    ]
    for params in paramExtremes:
        x, y = unzip(getLimitCycle(params))
        plt.plot(x, y, color='blue', alpha=0.7)
        plt.grid(True)
        plt.show()
