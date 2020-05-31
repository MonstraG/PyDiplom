import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *
from modelling.outliers.deterenisticOutliers.deterministicOutliers import repulsive

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

params = Params(0.01, 0.02, 0.13)
noise = 0.04
steps = 100000
startingPoint = Model.getStationaryPoint(params)
x, y = unzip(RK.genPointNoise(params, noise, steps, startingPoint))
plt.plot(x, y, color = 'blue', alpha = 0.5)
plt.plot(0, 0, alpha = 0)
plt.plot(2, 0, alpha = 0)
plt.title(f'Стохастические выбросы\nначало: {startingPoint}\n{params}\n'
          f'шаги: {steps}, шум: {noise}')
repulsive(params)
plt.show()
