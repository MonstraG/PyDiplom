from itertools import product

from defines import *

# [start, stop]
class Range:
    def __init__(self, start: float, step: float, stop: float):
        self.start = start
        self.step = step
        self.stop = stop
        self.current = self.start - self.step

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
    results = [RK.genPoint(params, 30000, Point(x, y))
               for x, y in product(xFor, yFor)]
    for line in results:
        x, y = unzip(line)
        plt.plot(x, y, color='blue', alpha=0.5)

def repulsive(params: Params):
    params.step = -params.step
    x, y = unzip(RK.genPoint(params, 1000, Point(0.5, 1.5)))
    plt.plot(x, y, color='red', alpha=0.5)

if __name__ == '__main__':
    params = Params(0.01, 0.02, 0.13)
    lines(params)
    repulsive(params)
    plt.show()
