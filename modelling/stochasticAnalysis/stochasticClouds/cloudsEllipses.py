from defines import *
from modelling.stochasticAnalysis.confidenceEllipse import drawEllipse

model = Model(step=0.01, a=0.1, b=0.3)
for noise in [0.001, 0.003]:
    x, y = unzip(RK.genPointNoise(model, steps=30000, noise=noise))
    plt.plot(x, y, color='blue', alpha=0.5)
    for probability in [0.65, 0.95, 0.99]:
        drawEllipse(model, noise, color='red', probability=probability)
    plt.show()
