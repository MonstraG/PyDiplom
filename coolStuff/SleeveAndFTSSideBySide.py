import matplotlib as mpl
import matplotlib.pyplot as plt

from coolStuff.fts import getFTS
from coolStuff.sleeve import sleevePlot
from defines import Params, transformPointList

mpl.rcParams['figure.dpi'] = 120

params = Params.defaultWithCycle()
noise = 0.03
reshuffleCycle = True

# sleeve
plt.subplot(121)
values_x, values_y = sleevePlot(params, noise, reshuffleCycle)
plt.plot(values_x[10000:], values_y[10000:], color = 'blue', alpha = 0.5, linewidth = 0.5)
plt.title(f'Sleeve and FTS, {params},')
plt.grid(True)

# fts
plt.subplot(122)
points = getFTS(params, None, reshuffleCycle)
x, y = transformPointList(points)
plt.plot(x, y, color = 'red', alpha = 0.7)
plt.grid(True)
plt.title(f' noise: {noise}, cycle: {"normal" if not reshuffleCycle else "reshuffled"}')
plt.show()

