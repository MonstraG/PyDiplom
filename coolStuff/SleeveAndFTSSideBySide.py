import matplotlib as mpl
import matplotlib.pyplot as plt

from coolStuff.fts import getFTS
from coolStuff.sleeve import sleevePlot
from defines import Params, unzip

mpl.rcParams['figure.dpi'] = 120

params = Params.defaultWithCycle()
noise = 0.03
reshuffleCycle = True

# sleeve
plt.subplot(121)
x, y = unzip(sleevePlot(params, noise, reshuffleCycle))
plt.plot(x[10000:], y[10000:], color = 'blue', alpha = 0.5, linewidth = 0.5)
plt.title(f'Sleeve and FTS, {params},')

# fts
plt.subplot(122)
x, y = unzip(getFTS(params, None, reshuffleCycle))
plt.plot(x, y, color = 'red', alpha = 0.7)
plt.grid(True)
plt.title(f' noise: {noise}, cycle: {"normal" if not reshuffleCycle else "reshuffled"}')
plt.show()
