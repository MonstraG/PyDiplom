from defines import *
from modelling.stochasticAnalysis.confidenceLines import sleevePlot

params = Params.defaultWithCycle()
params.step = 0.01
noise = 0.01

one_lap = 1500
# sleeve
plt.subplot(1, 2, 1)
steps = one_lap * 2
x, y = unzip(sleevePlot(params, noise, steps))
plt.plot(x, y, color='blue', alpha=0.5, linewidth=0.5)
plt.title(f'шаги={steps}')  # important

plt.subplot(1, 2, 2)
steps = one_lap * 20
x, y = unzip(sleevePlot(params, noise, steps))
plt.plot(x, y, color='blue', alpha=0.5, linewidth=0.5)
plt.title(f'шаги={steps}')  # important

plt.show()
