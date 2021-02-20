import numpy as np
import matplotlib.pyplot as plt

# .errorbar usage
sp = plt.subplot(211)
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()


# .fill_between usage
sp = plt.subplot(212)
x = np.arange(0, 10, 0.01)
plt.plot(x, x**2, label=r'$f = x^2$')
plt.scatter(x, x**2 + np.random.randn(len(x))*x, s=0.3)
plt.fill_between(x, 1.3*x**2, 0.7*x**2, alpha=0.3)
plt.legend(loc='best')

plt.show()
