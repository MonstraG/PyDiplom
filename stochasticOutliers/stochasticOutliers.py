from defines import *
import matplotlib as mpl
import matplotlib.pyplot as plt

from typing import List

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

def modelForAWhile(point: Point, params: Params, noise: float, steps: int) -> List[Point]:
    result = []
    current = point
    for _ in range(steps):
        result.append(current)
        current = RK.getNewPointWithNoise(current, params, noise = noise)
    return result

modelParams = Params(0.01, 0.02, 0.13)
noise = 0.05
steps = 1000000
# startingPoint = Point(.225, 3.5)
startingPoint = Model.getStationaryPoint(modelParams)
results = modelForAWhile(startingPoint, modelParams, noise, steps)
x, y = transformPointList(results)
plt.plot(x, y, color = 'blue', alpha = 0.33)
plt.title(f'Stochastic outliers\nstart: {startingPoint}\n{modelParams}\n'
          f'steps: {steps}, noise: {noise}')
plt.show()

