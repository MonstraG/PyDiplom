from defines import *
from modelling.stochasticAnalysis.confidenceEllipse import drawEllipse
from modelling.outliers.deterministic import lines, repulsive

params = Params(0.01, 0.02, 0.13)
noise_1, noise_2 = 0.01, 0.04
lines(params)
drawEllipse(params, noise_1, 'green')
drawEllipse(params, noise_2, 'red')
repulsive(params)
plt.show()
