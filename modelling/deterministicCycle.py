import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *

mpl.rcParams['figure.dpi'] = 120

number_of_steps = 300000
params = Params.defaultWithCycle()
st = Point(2, 0.4)
noise = 0.01
x, y = unzip(RK.genPointNoise(params, noise, number_of_steps, st))
plt.plot(x, y, color='blue', alpha=0.5)
plt.title(f'{params}, шум = {noise}')
plt.grid(True)
plt.show()

