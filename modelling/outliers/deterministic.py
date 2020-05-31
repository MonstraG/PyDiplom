from itertools import product
from typing import List

import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

# [start, stop]
class Range:
    def __init__(self, start: float, step: float, stop: float):
        self.start = start
        self.step = step
        self.stop = stop
        self.current = self.start - self.step

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.__class__.__name__}({self.start}, {self.step}, {self.stop})'

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current <= self.stop:
            return self.current
        raise StopIteration

def lines(params: Params):
    xFor = Range(.2, .05, .4)
    yFor = Range(3.0, .25, 3.5)
    results = [RK.genPoint(params, 30000, Point(x, y)) for x, y in product(xFor, yFor)]
    for line in results:
        x, y = unzip(line)
        plt.plot(x, y, color = 'blue', alpha = 0.5)
    plt.title(f'Детерменированные выбросы\nx: {xFor}, y: {yFor}\n{params}')

def repulsive(params: Params):
    params.step = -params.step
    startingPoints = [Point(0.5, 1.5)]

    results = [RK.genPoint(params, 1000, point) for point in startingPoints]
    for line in results:
        x, y = unzip(line)
        print(x[-1], y[-1])
        plt.plot(x, y, color = 'red', alpha = 0.5)

if __name__ == '__main__':
    params = Params(0.01, 0.02, 0.13)
    lines(params)
    repulsive(params)
    plt.show()
