import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

params = Params(0.01, 0.02, 0.13)
noise = 0.05
steps = 1000000
startingPoint = Model.getStationaryPoint(params)
x, y = unzip([_ for _ in RK.genPointNoise(params, noise, steps, startingPoint)])
plt.plot(x, y, color = 'blue', alpha = 0.33)
plt.title(f'Стохастические выбросы\nначало: {startingPoint}\n{params}\n'
          f'шаги: {steps}, шум: {noise}')
plt.show()
