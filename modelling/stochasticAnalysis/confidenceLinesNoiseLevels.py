from defines import *
from modelling.stochasticAnalysis.confidenceLines import sleevePlot

def drawConfidenceLines(model: Model, noise: float, steps: int):
    x, y = unzip(sleevePlot(model, noise, steps))
    plt.plot(x, y, color='blue', alpha=0.5, linewidth=0.5)
    plt.title(f'шаги={steps}')

one_lap = 1500  # approx
model = Model.defaultWithCycle(0.01)
noise = 0.01

plt.subplot(1, 2, 1)
drawConfidenceLines(model, noise, steps=one_lap * 2)
plt.subplot(1, 2, 2)
drawConfidenceLines(model, noise, steps=one_lap * 20)
plt.show()
