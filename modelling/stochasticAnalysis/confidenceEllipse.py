import math
import numpy
from defines import *

def drawEllipse(params: Params, noise: float, color: str = 'blue',
                probability: float = 0.95):
    p = Model.stationaryPoint(params)
    a, b, c, d = Model.getDifferentials(params)
    denominator = 2 * (a + d) * (a * d - b * c)
    w1 = (-b * c * d * sq(p.x) - a * sq(b) * sq(p.y)) / (a * denominator) - sq(p.x) / (2 * a)
    w2 = (a * b * sq(p.y) + c * d * sq(p.x)) / denominator
    w3 = (-sq(c) * d * sq(p.x) - a * b * c * sq(p.y)) / (d * denominator) - sq(p.y) / (2 * d)

    lambdas, vectors = numpy.linalg.eig([[w1, w2], [w2, w3]])
    lambda1, lambda2 = lambdas[0], lambdas[1]
    vector1, vector2 = (Point(vectors[0][0], vectors[0][1]),
                        Point(vectors[1][0], vectors[1][1]))

    resultX, resultY = [], []
    q = rt(-math.log(1 - probability))
    z1_, z2_ = noise * q * rt(2 * lambda1), noise * q * rt(2 * lambda2)
    for degrees in range(361):
        radians = math.radians(degrees)
        z1, z2 = z1_ * math.cos(radians), z2_ * math.sin(radians)
        resultX.append(p.x + (z1 * vector2.y - z2 * vector1.y))
        resultY.append(p.y + (z2 * vector1.x - z1 * vector2.x))
    plt.plot(resultX, resultY, color=color, alpha=0.5)
