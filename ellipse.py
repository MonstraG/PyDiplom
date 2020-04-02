import math
import numpy

from defines import *
import matplotlib as mpl
import matplotlib.pyplot as plt

matrixSolutionsCache = {}

# Produces ellipse, how big the cloud stochasticClouds should be
def drawEllipse(params: Params, noise: float, color: str = 'blue', probability: float = 0.95):
    def cacheLambdasAndVectors(params: Params, p: Point):
        a, b, c, d = Model.getDifferentials(params)
        denominator = 2 * (a + d) * (a * d - b * c)
        w1 = (-b * c * d * sq(p.x) - a * sq(b) * sq(p.y)) / (a * denominator) - sq(p.x) / (2 * a)
        w2 = (a * b * sq(p.y) + c * d * sq(p.x)) / denominator
        w3 = (-sq(c) * d * sq(p.x) - a * b * c * sq(p.y)) / (d * denominator) - sq(p.y) / (2 * d)

        lambdas, vectors = numpy.linalg.eig([[w1, w2], [w2, w3]])
        lambda1, lambda2 = lambdas[0], lambdas[1]
        vector1, vector2 = Point(vectors[0][0], vectors[0][1]), Point(vectors[1][0], vectors[1][1])
        matrixSolutionsCache[str(params)] = [lambda1, lambda2, vector1, vector2]

    p = Model.getStationaryPoint(params)
    cache = matrixSolutionsCache.get(str(params))
    if cache is None:
        cacheLambdasAndVectors(params, p)
    cache = matrixSolutionsCache.get(str(params))
    lambda1, lambda2, vector1, vector2 = cache

    resultX, resultY = [], []
    q = rt(-math.log(1 - probability))  # 0.95 - probability
    z1NoAngle, z2NoAngle = noise * q * rt(2 * lambda1), noise * q * rt(2 * lambda2)
    for i in range(361):
        radians = math.radians(i)
        z1, z2 = z1NoAngle * math.cos(radians), z2NoAngle * math.sin(radians)
        resultX.append(p.x + (z1 * vector2.y - z2 * vector1.y))
        resultY.append(p.y + (z2 * vector1.x - z1 * vector2.x))
    plt.plot(resultX, resultY, color = color, alpha = 0.5)

if __name__ == '__main__':
    drawEllipse(params = Params(0.01, 0.1, 0.3), noise = 0.001)
    mpl.rcParams['figure.dpi'] = 120
    plt.grid(True)
    plt.show()
