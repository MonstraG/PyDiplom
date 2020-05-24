import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import Params, RK, toStr, unzip
from confidenceEllipse import drawEllipse

mpl.rcParams['figure.dpi'] = 120

def mod_system_with_ellipses(params: Params, noise: float, steps: int = 30000):
    x, y = unzip(RK.genPointNoise(params, noise, steps))
    plt.plot(x, y, color = 'blue', alpha = 0.5)
    plt.title(f'{params}\n noise: {toStr(noise)}')
    for probability in confidence_levels:
        drawEllipse(params, noise, 'red', probability)
    plt.grid(True)
    plt.show()

params = Params(0.01, 0.1, 0.3)
noise_1, noise_2 = 0.003, 0.001
confidence_levels = [0.65, 0.95, 0.99]
mod_system_with_ellipses(params, noise_1)
mod_system_with_ellipses(params, noise_2)
