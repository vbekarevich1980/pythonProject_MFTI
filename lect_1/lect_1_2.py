import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5.01, 0.01)
plt.figure(figsize=(7, 7))
plt.plot(x, x*x - x - 6, label=r'$y(x)=x^2-x-6$')
plt.axhline(y=0, color='#d62728')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y(x)$', fontsize=14)
plt.title(r'$y(x)=x^2-x-6$', fontsize=20)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend_2.png')
plt.show()
