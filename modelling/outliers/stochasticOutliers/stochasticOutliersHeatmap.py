import time

import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *

mpl.rcParams['figure.dpi'] = 120

def drawHeatMap(noise: float, extent: [] = None, steps: int = 20000):
    points = []
    if extent is not None:
        points = [Point(extent[0], extent[2]), Point(extent[1], extent[3])]

    params = Params(0.01, 0.02, 0.13)
    startingPoint = Model.getStationaryPoint(params)
    startingPoint.y += 0.02  # somewhere near stationary point

    timestamps = []
    iterations = 300
    for i in range(iterations):
        startTime = time.time()
        points += [_ for _ in RK.genPointNoise(params, noise, steps, startingPoint)]
        timestamps.append(time.time() - startTime)
        eta = (iterations - i) * sum(timestamps) / len(timestamps)
        print(f'Закочил итерацию {i}, прошло: {toStr(sum(timestamps))} сек., Осталось: {toStr(eta)} Сек.')

    x, y = unzip(points)
    heatMap, xedges, yedges = np.histogram2d(x, y, bins = (300, 222))
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    aspect = (extent[1] - extent[0]) / (extent[3] - extent[2])

    heatMap = log(heatMap)

    plt.imshow(heatMap.T, extent = extent, aspect = aspect, origin = 'lower')
    return extent

def log(matrix):
    with np.errstate(divide = 'ignore'):
        res = np.log2(matrix)
        res[np.isneginf(res)] = 0
        return res

plt.subplot(1, 2, 1)
extent = drawHeatMap(0.3)

plt.subplot(1, 2, 2)
_ = drawHeatMap(0.05, extent)
plt.show()
