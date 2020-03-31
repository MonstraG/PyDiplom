import matplotlib as mpl
import matplotlib.pyplot as plt

from defines import Params, Model, Point, RK

mpl.rcParams['figure.dpi'] = 120
plt.grid(True)

def plot_graphs(title: str, x_array, y_array):
    plt.plot(x_array, y_array, color='blue', alpha=0.5)
    plt.title(title)

def mod_system(current: Point, params: Params):
    values_x, values_y = [current.x], [current.y]
    for _ in range(number_of_steps):
        current = RK.getNewPoint(current, params)
        values_x.append(current.x)
        values_y.append(current.y)
    plot_graphs(str(params), values_x, values_y)

step, number_of_steps = 0.01, 30000
posShifts = [0.01, 0.25, 0.5]
negShifts = [-x for x in posShifts]
shifts_x = posShifts + negShifts + posShifts + negShifts
shifts_y = posShifts + posShifts + negShifts + negShifts
for i in range(5):
    a, b = 0.06, i / 5.0 + 0.2
    params = Params(step, a, b)
    point = Model.getStationaryPoint(params)
    for shift_x, shift_y in zip(shifts_x, shifts_y):
        point = Point(point.x + shift_x, point.y + shift_y)
        mod_system(point, params)
    plt.grid(True)
    plt.show()
