from defines import *
from modelling.outliers.deterministic import repulsive

params = Params(0.01, 0.02, 0.13)
noise = 0.04
steps = 100000
startingPoint = Model.stationaryPoint(params)
x, y = unzip(RK.genPointNoise(params, noise, steps, startingPoint))
plt.plot(x, y, color='blue', alpha=0.5)
plt.plot(0, 0, alpha=0)
plt.plot(2, 0, alpha=0)
repulsive(params)
plt.show()
