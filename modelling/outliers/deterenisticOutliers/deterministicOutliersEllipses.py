import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *
from modelling.outliers.deterenisticOutliers.deterministicOutliers import lines, repulsive
from modelling.confidenceEllipse import drawEllipse

mpl.rcParams['figure.dpi'] = 120

params = Params(0.01, 0.02, 0.13)
noise_1, noise_2 = 0.01, 0.04

lines(params)
drawEllipse(params, noise_1, 'green')
drawEllipse(params, noise_2, 'red')
repulsive(params)
plt.grid(True)
plt.suptitle(f'Малый шум: {noise_1}, большой: {noise_2}', y=0.05)
plt.show()
