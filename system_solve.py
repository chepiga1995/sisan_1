import numpy as np


def gradient_descent(A, b, eps):
    m = len(A.T)
    x = np.zeros(shape=(m,1))
    i = 0
    imax = 100000
    r = b - A * x
    delta = r.T * r
    delta0 = delta
    while i < imax and delta > eps ** 2 * delta0:
        alpha = float(delta / (r.T * (A * r)))
        x = x + alpha * r
        r = b - A * x
        delta = r.T * r
        i += 1

    return x
# a = np.matrix([[1, 0], [0, 1]])
# b = np.matrix([[1], [1]])
# res = conjugate_gradient_method(a, b, 0.001);
# print(res)