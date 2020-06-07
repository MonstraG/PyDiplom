from defines import *
from modelling.stochasticAnalysis.confidenceEllipse import drawEllipse

params = Params(0.01, 0.1, 0.3)
for noise in [0.001, 0.003]:
    x, y = unzip(RK.genPointNoise(params, noise, 30000))
    plt.plot(x, y, color='blue', alpha=0.5)
    for probability in [0.65, 0.95, 0.99]:
        drawEllipse(params, noise, 'red', probability)
    plt.show()
