from defines import *
from modelling.outliers.deterministic import lines, repulsive
from modelling.stochasticAnalysis.confidenceEllipse import drawEllipse

model = Model(step=0.01, a=0.02, b=0.13)
lines(model)
drawEllipse(model=model, noise=0.01, color='green')
drawEllipse(model=model, noise=0.04, color='red')
repulsive(model)
plt.show()
