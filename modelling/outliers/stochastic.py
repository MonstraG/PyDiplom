from defines import *
from modelling.outliers.deterministic import repulsive

model = Model(step=0.01, a=0.02, b=0.13)
x, y = unzip(RK.genPointNoise(model=model, steps=1000000, noise=0.04,
                              current=model.stationaryPoint))
plt.plot(x, y, color='blue', alpha=0.5)
plt.plot(0, 0, alpha=0)
plt.plot(2, 0, alpha=0)
repulsive(model)
plt.show()
