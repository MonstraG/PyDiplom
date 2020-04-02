import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import Params, Model, RK, toStr
from ellipse import drawEllipse

mpl.rcParams['figure.dpi'] = 120

def plot(params: Params, values_x, values_y, noise: float):
    plt.plot(values_x, values_y, color = 'blue', alpha = 0.5)
    plt.title(f'{params}\n noise: {toStr(noise)}')

def mod_system_with_ellipses(params: Params, noise: float):
    current = Model.getStationaryPoint(params)
    values_x, values_y = [current.x], [current.y]
    for _ in range(30000):
        current = RK.getNewPointWithNoise(current, params, noise)
        values_x.append(current.x)
        values_y.append(current.y)
    plot(params, values_x, values_y, noise)
    for probability in confidence_levels:
        drawEllipse(params, noise, 'red', probability)
    plt.grid(True)
    plt.show()

params = Params(0.01, 0.1, 0.3)
noise_1, noise_2 = 0.003, 0.001
confidence_levels = [0.65, 0.95, 0.99]
mod_system_with_ellipses(params, noise_1)
mod_system_with_ellipses(params, noise_2)
