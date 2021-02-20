import numpy as np
import matplotlib.pyplot as plt

# Hardy G. H. Weierstrass’s nondifferentiable function


M = 1000000
a = 3
b = 0.5


def weierstrass(x, N):
	y = np.zeros((1, M))
	for n in range(1, N):
		y = y + np.cos(a ** n * np.pi * x) * b ** n
	return y


x_data = np.linspace(-2, 2, M)
y_data = np.reshape(weierstrass(x_data, 500), (M,))

plt.figure(figsize=(11, 7))
plt.plot(x_data, y_data, 'r-')
plt.grid()
plt.show()
