import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 120

b_1 = lambda a: ((1 - 2 * a + (1 - 8 * a) ** .5) / 2) ** .5
b_2 = lambda a: ((1 - 2 * a - (1 - 8 * a) ** .5) / 2) ** .5

values_b1, values_b2, values_a = [], [], []
a = 0.0
while a < 0.126:
    values_a.append(a)
    values_b1.append(b_1(a).real)
    values_b2.append(b_2(a).real)
    a += 0.001
plt.plot(values_a, values_b1, values_a, values_b2, color='blue')
plt.xlabel('a')
plt.ylabel('b')
plt.text(0.055, 0.6, 'X', fontsize=18)
plt.text(0.11, 0.25, 'Y', fontsize=18)
plt.grid(True)
plt.show()
