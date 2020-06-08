from itertools import chain

from defines import *

def drawHeatMap(iterations: int, noise: float, steps: int, extent: []):
    points = []
    if extent is not None:
        points = [Point(extent[0], extent[2]),
                  Point(extent[1], extent[3])]
    model = Model(step=0.01, a=0.02, b=0.13)
    for i in range(iterations):
        points += RK.genPointNoise(model, steps, noise,
                                   current=model.stationaryPoint)

    x, y = unzip(points)
    heatMap, x_edges, y_edges = np.histogram2d(x, y, bins=(300, 222))
    extent = [x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]]
    aspect = (extent[1] - extent[0]) / (extent[3] - extent[2])

    plt.imshow(log(heatMap).T, extent=extent, aspect=aspect, origin='lower')
    return extent

def log(matrix):
    with np.errstate(divide='ignore'):
        res = np.log2(matrix)
        res[np.isneginf(res)] = 0
        return res

iterations = 1
steps = 30000
plt.subplot(1, 2, 2)
noise = 0.04
plt.title(f'шум={noise}')
extent = drawHeatMap(iterations, noise, steps, None)
plt.subplot(1, 2, 1)
noise = 0.01
plt.title(f'шум={noise}')
_ = drawHeatMap(iterations, noise, steps, extent)
plt.show()
