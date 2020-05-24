import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import Params, Model, Point, RK, unzip

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

step, number_of_steps = 0.01, 30000
posShifts = [0.05, 0.15]
negShifts = [-x for x in posShifts]
shifts_x = posShifts + negShifts + posShifts + negShifts
shifts_y = posShifts + posShifts + negShifts + negShifts
a, b = 0.06, 0.0
for _ in range(5):
    b += 0.2
    params = Params(step, a, b)
    stPoint = Model.getStationaryPoint(params)
    for shift_x, shift_y in zip(shifts_x, shifts_y):
        point = Point(stPoint.x + shift_x, stPoint.y + shift_y)
        x, y = unzip([x for x in RK.genPoint(params, number_of_steps, point)])
        plt.plot(x, y, color = 'blue', alpha = 0.5)
    plt.title(params)
    plt.grid(True)
    plt.show()
