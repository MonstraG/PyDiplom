import math

from defines import *
from modelling.stochasticAnalysis.limitCycle import getLimitCycle

# Stochastic sensitivity function
def getSSF(params: Params, limitCycle: []):
    r, h = [1.0], [0.0]
    fx, fy, gx, gy = Model.getDifferentials(params)
    for cyclePoint in limitCycle:
        p = Model.getSystemPointNormalized(cyclePoint, params)
        a = (p.x * (p.x * (gx + fy) + p.x * 2 * fx) +
             p.y * (p.y * (gx + fy) + p.y * 2 * gy))
        r.append(r[-1] * math.e ** (a * params.step))
        b = sq(p.x) * sq(cyclePoint.x) + sq(p.y) * sq(cyclePoint.y)
        h.append(h[-1] + b / r[-1] * params.step)

    c = r[-1] * h[-1] / (1 - r[-1])
    return [Point(i * params.step, rr * (c + hh))
            for i, [rr, hh] in enumerate(zip(r, h))]

def rearrange(a_list: []) -> []:
    half = len(a_list) // 2
    return a_list[half:] + a_list[:half]

if __name__ == '__main__':
    params = Params.defaultWithCycle()
    _, y = unzip(rearrange(getSSF(params, getLimitCycle(params))))
    plt.plot(y, color='red', alpha=0.7)
    plt.grid(True)
    plt.show()
