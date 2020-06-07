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
plt.show()
