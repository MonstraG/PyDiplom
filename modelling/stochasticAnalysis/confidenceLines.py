from defines import *
from modelling.stochasticAnalysis.SSF import getSSF
from modelling.stochasticAnalysis.limitCycle import getLimitCycle

def sleevePlot(model: Model, noise: float, steps: int):
    q = 1.386  # 0.95, 1/erf(0.95)
    limitCycle = getLimitCycle(model)
    result1, result2 = [], []
    for cycleP, fts in zip(limitCycle, getSSF(model, limitCycle)):
        normalPoint = model.getSystemPointNormalized(cycleP)
        multiplier = q * noise * rt(2 * fts.y)
        shiftX, shiftY = (multiplier * normalPoint.x * cycleP.x,
                          multiplier * normalPoint.y * cycleP.y)
        result1.append(Point(cycleP.x + shiftX, cycleP.y + shiftY))
        result2.append(Point(cycleP.x - shiftX, cycleP.y - shiftY))
    x, y = unzip(result1)
    plt.plot(x, y, color='red', alpha=0.7)
    x, y = unzip(result2)
    plt.plot(x, y, color='red', alpha=0.7)
    return RK.genPointNoise(model, steps, noise, Point(2, 0.1))

if __name__ == '__main__':
    model = Model.defaultWithCycle()
    x, y = unzip(sleevePlot(model, noise=0.02, steps=5000000))
    plt.plot(x, y, color='blue', alpha=0.5, linewidth=0.5)
    x, y = unzip(getLimitCycle(model))
    plt.plot(x, y, color='green', alpha=0.7)
    plt.show()
