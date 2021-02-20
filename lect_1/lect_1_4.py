import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
y = input('Введите функцию для построения графика с переменной "x"\n')


def foo_1(x_var, y_var):
    try:
        plt.figure(figsize=(11, 7))
        with plt.xkcd():
            plt.plot(x_var, eval(y_var), label='f(x)=' + y_var)
            plt.xlabel(r'$x$', fontsize=14)
            plt.ylabel(r'$f(x)$', fontsize=14)
            plt.title('f(x)=' + y_var, fontsize=15)
            plt.grid(True)
            plt.legend(loc='lower right', fontsize=12)
            plt.savefig('figure_with_legend_3.png')
            plt.show()
    except Exception:
        print('Введеные данные не являются функцией\n')
        y_var = input('Введите функцию для построения графика с переменной "x"\n')
        foo_1(x_var, y_var)


foo_1(x, y)
