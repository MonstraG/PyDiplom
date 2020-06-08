from defines import *

model = Model(step=0.01, a=0.1, b=0.3)
steps = 30000
x, y = unzip(RK.genPointNoise(model, steps, noise=0.003))
plt.plot(x, y, color='red', alpha=0.5)
x, y = unzip(RK.genPointNoise(model, steps, noise=0.001))
plt.plot(x, y, color='blue', alpha=0.5)
plt.show()
