import numpy as np


def mul_v(my_vector: []):
    a = np.array(my_vector, int)
    return np.outer(a,a)


def mul_m(W,V):
    V = np.array(V, int)
    V_1 = W.dot(V)
    print(V_1)
    return [int(_/abs(_)) for _ in V_1]

def sum_m(w1, w2):
    return np.add(w1, w2)


def fill_diagonal(W):
    a = np.diagonal(W)
    a.setflags(write=True)
    a.fill(0)
    return W

