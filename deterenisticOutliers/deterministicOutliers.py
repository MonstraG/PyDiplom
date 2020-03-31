from defines import *
import matplotlib as mpl
import matplotlib.pyplot as plt

from typing import List

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

def modelFor(point: Point, params: Params, amount: int) -> List[Point]:
    result = []
    current = point
    for _ in range(amount):
        result.append(current)
        current = RK.getNewPoint(current, params)
    return result

class For:
    def __init__(self, start: float, step: float, stop: float):
        self.start = start
        self.step = step
        self.stop = stop

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'For({self.start}, {self.step}, {self.stop})'

def lines(params: Params):
    startingPoints = []
    xFor = For(.2, .05, .4)
    yFor = For(3.0, .25, 3.5)
    x = xFor.start
    while x <= xFor.stop:
        y = yFor.start
        while y <= yFor.stop:
            startingPoints.append(Point(x, y))
            y += yFor.step
        x += xFor.step

    results = [modelFor(point, params, 5000) for point in startingPoints]

    for line in results:
        x, y = transformPointList(line)
        plt.plot(x, y, color = 'blue', alpha = 0.5)
    plt.title(f'Deterministic outliers\nx: {xFor}, y: {yFor}\n{params}')

def repulsive(params: Params):
    params.step = -params.step
    startingPoints = [Point(0.5, 1.5)]

    results = [modelFor(point, params, 1000) for point in startingPoints]

    for line in results:
        x, y = transformPointList(line)
        plt.plot(x, y, color = 'red', alpha = 0.5)

if __name__ == '__main__':
    params = Params(0.01, 0.02, 0.13)
    lines(params)
    repulsive(params)
    plt.show()
