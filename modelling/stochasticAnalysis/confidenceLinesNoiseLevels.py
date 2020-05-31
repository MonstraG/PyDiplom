import matplotlib as mpl
import matplotlib.pyplot as plt

from modelling.stochasticAnalysis.confidenceLines import sleevePlot
from defines import Params, unzip

mpl.rcParams['figure.dpi'] = 120

params = Params.defaultWithCycle()
params.step = 0.01
noise = 0.01

one_lap = 1500
# sleeve
plt.subplot(121)
steps = one_lap * 2
x, y = unzip(sleevePlot(params, noise, False, steps))
plt.plot(x, y, color = 'blue', alpha = 0.5, linewidth = 0.5)
plt.title(f'шаги={steps}')
plt.grid(True)

plt.subplot(122)
steps = one_lap * 20
x, y = unzip(sleevePlot(params, noise, False, steps))
plt.plot(x, y, color = 'blue', alpha = 0.5, linewidth = 0.5)
plt.title(f'шаги={steps}')
plt.grid(True)

plt.suptitle(f'Доверительная полоса и ФСЧ, {params}')
plt.show()
