from defines import *

def drawHeatMap(iterations: int, noise: float,  steps: int, extent: [] = None):
    points = []
    if extent is not None:
        points = [Point(extent[0], extent[2]),
                  Point(extent[1], extent[3])]

    params = Params(0.01, 0.02, 0.13)
    startingPoint = Model.stationaryPoint(params)

    for i in range(iterations):
        points += RK.genPointNoise(params, noise, steps, startingPoint)

    x, y = unzip(points)
    heatMap, xedges, yedges = np.histogram2d(x, y, bins=(300, 222))
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    aspect = (extent[1] - extent[0]) / (extent[3] - extent[2])

    plt.imshow(log(heatMap).T, extent=extent, aspect=aspect, origin='lower')
    return extent

def log(matrix):
    with np.errstate(divide='ignore'):
        res = np.log2(matrix)
        res[np.isneginf(res)] = 0
        return res

iterations = 50
steps = 30000
plt.subplot(1, 2, 1)
noise = 0.01
plt.title(f'шум={noise}')
extent = drawHeatMap(iterations, noise, steps, None)
plt.subplot(1, 2, 2)
noise = 0.04
plt.title(f'шум={noise}')
_ = drawHeatMap(iterations, noise, steps, extent)
plt.show()
