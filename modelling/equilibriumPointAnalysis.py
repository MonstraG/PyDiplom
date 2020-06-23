from defines import *

b_1 = lambda a: ((1 - 2 * a + (1 - 8 * a) ** .5) / 2) ** .5
b_2 = lambda a: ((1 - 2 * a - (1 - 8 * a) ** .5) / 2) ** .5

values_a, values_b1, values_b2 = [], [], []
a = 0.0
while a < 0.126:
    values_a.append(a)
    values_b1.append(b_1(a).real)
    values_b2.append(b_2(a).real)
    a += 0.001
plt.plot(values_a, values_b1, values_a, values_b2, color='blue')
plt.xlabel('a')
plt.ylabel('b')
plt.text(0.05, 0.5, 'X', fontsize=14)
plt.text(0.088, 0.23, 'Y', fontsize=14)
plt.plot(0.005, 0.95, 'ro')
step = 0
models = [
    Model(step, 0.005, 0.95),
    Model(step, 0.06, 0.85),
    Model(step, 0.1, 0.75),
    Model(step, 0.005, 0.6),
    Model(step, 0.06, 0.6),
    Model(step, 0.12, 0.6),
    Model(step, 0.005, 0.1),
    Model(step, 0.06, 0.35),
    Model(step, 0.1, 0.45)
]
for model in models:
    plt.plot(model.a, model.b, 'ro')

plt.show()
