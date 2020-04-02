import matplotlib.pyplot as plt

from defines import RK, Model, Point, Params, transformPointList

def getLimitCycle(params: Params, intersectEpsilon: float = 0.000001):
    current = Point(1.0, 1.0)
    result = []
    stPoint = Model.getStationaryPoint(params)
    x0, y0 = stPoint.x, stPoint.y
    curIntersect = None
    while True:
        newPoint = RK.getNewPoint(current, params)
        if (current.y - y0) * (newPoint.y - y0) < 0 and current.x > x0 and newPoint.x > x0:
            newIntersect = ((-(newPoint.x - current.x) * y0 - (current.x * newPoint.y - newPoint.x * current.y)) / (current.y - newPoint.y))
            if curIntersect is not None and abs(newIntersect - curIntersect) < intersectEpsilon:
                current = Point(newIntersect, y0)
                while not ((current.y - y0) * (newPoint.y - y0) < 0 and current.x > x0 and newPoint.x > x0):
                    result.append(newPoint)
                    current = Point(newPoint.x, newPoint.y)
                    newPoint = RK.getNewPoint(current, params)
                result.append(newPoint)
                result.append(result[0])
                return result
            curIntersect = newIntersect
        current = Point(newPoint.x, newPoint.y)

if __name__ == '__main__':
    params = Params.defaultWithCycle()
    intersectEpsilon = 0.000001
    points = getLimitCycle(params, intersectEpsilon)

    x, y = transformPointList(points)
    plt.plot(x, y, color='blue', alpha=0.7)

    plt.title(f'Limit cycle (intersectEpsilon: {intersectEpsilon})\n {params}')
    plt.grid(True)
    plt.show()
    