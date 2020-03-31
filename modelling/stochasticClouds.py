import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import Params, Model, RK, toStr

mpl.rcParams['figure.dpi'] = 120

def mod_system_with_noise(params: Params, noise: float, color: str):
    current = Model.getStationaryPoint(params)
    values_x, values_y = [current.x], [current.y]
    for _ in range(30000):
        current = RK.getNewPointWithNoise(current, params, noise)
        values_x.append(current.x)
        values_y.append(current.y)
    plt.plot(values_x, values_y, color = color, alpha = 0.5)

params = Params(0.01, 0.1, 0.3)
noise_1, noise_2 = 0.003, 0.001
mod_system_with_noise(params, noise_1, 'blue')
mod_system_with_noise(params, noise_2, 'red')
plt.title(f'{params}\n outer cloud noise: {toStr(max(noise_1, noise_2))}, inner cloud noise: {toStr(min(noise_1, noise_2))}')
plt.grid(True)
plt.show()
