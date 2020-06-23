from defines import *
from modelling.outliers.deterministic import repulsive

model = Model(step=0.01, a=0.02, b=0.13)
plt.subplot(1, 2, 2)
x, y = unzip(RK.genPointNoise(model=model, steps=100000, noise=0.04,
                              current=model.stationaryPoint))
plt.plot(x, y, color='blue', alpha=0.5)
extent = [[min(x), max(x)], [min(y), max(y)]]
repulsive(model)
plt.grid(True)

plt.subplot(1, 2, 1)
x, y = unzip(RK.genPointNoise(model=model, steps=100000, noise=0.01,
                              current=model.stationaryPoint))
plt.plot(extent[0], extent[1], alpha=0)
plt.plot(x, y, color='blue', alpha=0.5)
plt.grid(True)
plt.show()
