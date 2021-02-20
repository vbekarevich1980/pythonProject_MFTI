import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(11, 7))
plt.plot(x, np.log((x ** 2 + 1) * (np.exp(abs(x) / -10))) / np.log(1 + np.tan(1 / (1 + np.sin(x) ** 2))),
         label=r'$f(x)=\log_{1+\tan(\frac{1}{1+\sin^2(x)})}(x^2+1)\exp(-\frac{|x|}{10})$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.title(r'$f(x)=\log_{1+\tan(\frac{1}{1+\sin^2(x)})}(x^2+1)\exp(-\frac{|x|}{10})$', fontsize=15)
plt.grid(True)
plt.legend(loc='lower right', fontsize=12)
plt.savefig('figure_with_legend_3.png')
plt.show()
