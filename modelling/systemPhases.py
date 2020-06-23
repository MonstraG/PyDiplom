from defines import *

step, number_of_steps = 0.01, 30000
posShifts = [0.05, 0.15]
negShifts = [-x for x in posShifts]
shifts_x = posShifts + negShifts + posShifts + negShifts
shifts_y = posShifts + posShifts + negShifts + negShifts
models = [
    Model(step, 0.02, 0.9),
    Model(step, 0.07, 0.9),
    Model(step, 0.12, 0.9),
    Model(step, 0.02, 0.6),
    Model(step, 0.07, 0.6),
    Model(step, 0.12, 0.6),
    Model(step, 0.02, 0.2),
    Model(step, 0.07, 0.2),
    Model(step, 0.12, 0.2)
]
for i, model in enumerate(models):
    for shift_x, shift_y in zip(shifts_x, shifts_y):
        point = Point(abs(model.stationaryPoint.x + shift_x * (5 * model.b)),
                      abs(model.stationaryPoint.y + shift_y * (5 * model.b)))
        x, y = unzip(RK.genPoint(model, number_of_steps, point))
        plt.subplot(3, 3, i + 1)
        plt.plot(x, y, color='blue', alpha=0.5)
    plt.grid(True)

plt.show()
