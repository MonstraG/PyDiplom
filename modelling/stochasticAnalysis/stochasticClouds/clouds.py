from defines import *

params = Params(step=0.01, a=0.1, b=0.3)
steps = 30000
x, y = unzip(RK.genPointNoise(params, 0.003, steps))
plt.plot(x, y, color='red', alpha=0.5)
x, y = unzip(RK.genPointNoise(params, 0.001, steps))
plt.plot(x, y, color='blue', alpha=0.5)
plt.show()
