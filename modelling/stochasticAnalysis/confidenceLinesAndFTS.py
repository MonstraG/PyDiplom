import matplotlib as mpl
import matplotlib.pyplot as plt

from modelling.stochasticAnalysis.FTS import getFTS
from modelling.stochasticAnalysis.confidenceLines import sleevePlot
from defines import Params, unzip

mpl.rcParams['figure.dpi'] = 120

params = Params.defaultWithCycle()
noise = 0.03
reshuffleCycle = True

# sleeve
plt.subplot(121)
x, y = unzip(sleevePlot(params, noise, reshuffleCycle))
plt.plot(x[10000:], y[10000:], color = 'blue', alpha = 0.5, linewidth = 0.5)
plt.title(f'Доверительная полоса и ФСЧ, {params},')

# fts
plt.subplot(122)
x, y = unzip(getFTS(params, None, reshuffleCycle))
plt.plot(x, y, color = 'red', alpha = 0.7)
plt.grid(True)
plt.title(f' шум: {noise}, {"цикл обращен" if reshuffleCycle else ""}')
plt.show()
