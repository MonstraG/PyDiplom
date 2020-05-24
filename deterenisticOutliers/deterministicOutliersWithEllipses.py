import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import *
from deterenisticOutliers.deterministicOutliers import lines, repulsive
from confidenceEllipse import drawEllipse

mpl.rcParams['figure.dpi'] = 120

params = Params(0.01, 0.02, 0.13)

lines(params)
drawEllipse(params, 0.01, 'green')
drawEllipse(params, 0.03, 'red')
repulsive(params)
plt.grid(True)
plt.show()
