from defines import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

mpl.rcParams['figure.dpi'] = 120

def theThing(noise: float, extent: [] = None):
    points = []
    if extent is not None:
        points = [Point(extent[0], extent[2]), Point(extent[1], extent[3])]
    def modelForAWhile(point: Point, params: Params):
        current = point
        for _ in range(20000):
            points.append(current)
            current = RK.getNewPointWithNoise(current, params, noise)

    params = Params(0.01, 0.02, 0.13)
    startingPoint = Model.getStationaryPoint(params)
    startingPoint.y += 0.02

    timestamps = []
    iterations = 300
    for i in range(iterations):
        startTime = time.time()
        modelForAWhile(startingPoint, params)
        elapsedTime = time.time() - startTime

        timestamps.append(elapsedTime)
        eta = (iterations - i) * sum(timestamps) / len(timestamps)
        print(f'Finished iteration {i}, elapsed time: {format(sum(timestamps), ".3f")} sec., ETA: {format(eta, ".3f")} sec.')

    x, y = transformPointList(points)
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=(300, 222))
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    aspect = (extent[1] - extent[0]) / (extent[3] - extent[2])

    def log(matrix):
        with np.errstate(divide = 'ignore'):
            res = np.log2(matrix)
            res[np.isneginf(res)] = 0
            return res

    heatmap = log(heatmap)

    plt.imshow(heatmap.T, extent=extent, aspect=aspect, origin='lower')
    return extent


plt.subplot(1, 2, 1)
extent = theThing(0.3)

plt.subplot(1, 2, 2)
_ = theThing(0.05, extent)
plt.show()
