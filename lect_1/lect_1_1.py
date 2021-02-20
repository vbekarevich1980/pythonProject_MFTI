import numpy as np


def calculation(x):
    """calculation of the algebraic expression """
    y = np.log((1 / (np.e ** (np.sin(x) + 1))) / (5 / 4 + 1 / (x ** (1 / 5)))) / np.log(1 + x ** 2)
    print(y)


calculation(1)

calculation(10)

calculation(1000)
