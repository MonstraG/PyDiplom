from defines import *

step, number_of_steps = 0.01, 30000
posShifts = [0.05, 0.15]
negShifts = [-x for x in posShifts]
shifts_x = posShifts + negShifts + posShifts + negShifts
shifts_y = posShifts + posShifts + negShifts + negShifts
a, b = -0.02, 0.6
for _ in range(2):
    a += 0.04
    model = Model(step, a, b)
    for shift_x, shift_y in zip(shifts_x, shifts_y):
        point = Point(abs(model.stationaryPoint.x + shift_x * (10 * b)),
                      abs(model.stationaryPoint.y + shift_y * (10 * b)))
        x, y = unzip(RK.genPoint(model, number_of_steps, point))
        plt.plot(x, y, color='blue', alpha=0.5)
    plt.grid(True)
    plt.show()
