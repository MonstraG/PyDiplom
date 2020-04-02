from defines import *
import matplotlib as mpl
import matplotlib.pyplot as plt

from deterenisticOutliers.deterministicOutliers import lines, repulsive
from ellipse import drawEllipse

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

params = Params(0.01, 0.02, 0.13)

lines(params)
drawEllipse(params, 0.01, 'green')
drawEllipse(params, 0.03, 'red')
repulsive(params)
plt.show()
