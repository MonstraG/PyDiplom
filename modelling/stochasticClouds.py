import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import Params, RK, toStr, unzip

mpl.rcParams['figure.dpi'] = 120

params = Params(0.01, 0.1, 0.3)
noise_1, noise_2 = 0.003, 0.001
steps = 30000
x, y = unzip(RK.genPointNoise(params, noise_1, steps))
plt.plot(x, y, color = 'blue', alpha = 0.5)
x, y = unzip(RK.genPointNoise(params, noise_2, steps))
plt.plot(x, y, color = 'red', alpha = 0.5)
plt.title(f'{params}\n outer cloud noise: {toStr(max(noise_1, noise_2))}, '
          f'inner cloud noise: {toStr(min(noise_1, noise_2))}')
plt.grid(True)
plt.show()
