import math

from defines import *
from modelling.stochasticAnalysis.limitCycle import getLimitCycle

# Stochastic sensitivity function
def getSSF(model: Model, limitCycle: []):
    r, h = [1.0], [0.0]
    fx, fy, gx, gy = model.differentials
    for cyclePoint in limitCycle:
        np = model.getSystemPointNormalized(cyclePoint)
        a = (np.x * (np.x * (gx + fy) + np.x * 2 * fx) +
             np.y * (np.y * (gx + fy) + np.y * 2 * gy))
        r.append(r[-1] * math.e ** (a * model.step))
        b = sq(np.x) * sq(cyclePoint.x) + sq(np.y) * sq(cyclePoint.y)
        h.append(h[-1] + b / r[-1] * model.step)

    c = r[-1] * h[-1] / (1 - r[-1])
    return [Point(i * model.step, rr * (c + hh))
            for i, [rr, hh] in enumerate(zip(r, h))]

def rearrange(a_list: []) -> []:
    half = len(a_list) // 2
    return a_list[half:] + a_list[:half]

if __name__ == '__main__':
    model = Model.defaultWithCycle()
    _, y = unzip(rearrange(getSSF(model, getLimitCycle(model))))
    plt.plot(y, color='red', alpha=0.7)
    plt.grid(True)
    plt.show()
