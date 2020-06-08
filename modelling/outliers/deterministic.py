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

def lines(model: Model):
    xFor = Range(.2, .05, .4)
    yFor = Range(3.0, .25, 3.5)
    results = [RK.genPoint(model, steps=30000, current=Point(x, y))
               for x, y in product(xFor, yFor)]
    for line in results:
        x, y = unzip(line)
        plt.plot(x, y, color='blue', alpha=0.5)

def repulsive(model: Model):
    model.step = -model.step
    x, y = unzip(RK.genPoint(model=model, steps=1000,
                             current=Point(0.5, 1.5)))
    plt.plot(x, y, color='red', alpha=0.5)

if __name__ == '__main__':
    model = Model(step=0.01, a=0.02, b=0.13)
    lines(model)
    repulsive(model)
    plt.show()
