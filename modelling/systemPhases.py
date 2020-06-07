from defines import *

step, number_of_steps = 0.01, 30000
posShifts = [0.05, 0.15]
negShifts = [-x for x in posShifts]
shifts_x = posShifts + negShifts + posShifts + negShifts
shifts_y = posShifts + posShifts + negShifts + negShifts
a, b = 0.06, 0.0
for _ in range(5):
    b += 0.2
    params = Params(step, a, b)
    stPoint = Model.stationaryPoint(params)
    for shift_x, shift_y in zip(shifts_x, shifts_y):
        point = Point(abs(stPoint.x + shift_x * (10 * b)),
                      abs(stPoint.y + shift_y * (10 * b)))
        x, y = unzip(RK.genPoint(params, number_of_steps, point))
        plt.plot(x, y, color='blue', alpha=0.5)
    plt.grid(True)
    plt.show()
