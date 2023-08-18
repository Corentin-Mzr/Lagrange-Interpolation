import matplotlib.pyplot as plt
import numpy as np


def l_i(x: float, X: list[float], i:int) -> float:
    """
    x: Evaluation point
    X: Set of nodes of length n
    i: Index of i-th node
    Return the n + 1 lagrange polynomial evaluated in x
    """
    p = 1
    for j in range(len(X)):
        if j != i:
            p *= (x - X[j])/(X[i] - X[j])
    return p


def lagrange_interpolation(x:float, X: list[float], Y: list[float]) -> float:
    """
    x: Evaluation point
    X: X-coordinates of interpolation points
    Y: Y-coordinates of interpolation points
    Return the interpolation formula evaluated in x
    """
    s = 0
    for i in range(len(X)):
        s += Y[i] * l_i(x, X, i)
    return s


def f(X: np.array) -> np.array:
    return np.exp(-X) - np.sqrt(abs(X)) - X**2


if __name__ == "__main__":
    # Interval of x
    xmin,xmax = -5,5

    # Set of points
    n = 5
    X = np.linspace(xmin,xmax,n)
    Y = f(X)

    # Interpolation
    sub_n = 100
    subX = np.linspace(xmin,xmax,sub_n)
    I = [lagrange_interpolation(x, X, Y) for x in subX]

    # Real values
    realY = f(subX)

    # Plot
    plt.close()
    fig, ax = plt.subplots()

    nodes = ax.scatter(X, Y)
    interpolation, = ax.plot(subX, I, "r")
    real, = ax.plot(subX, realY, "g")

    fig.legend((nodes, interpolation, real), ("Given points", "Interpolation", "Real curve"))
    plt.title("Lagrange Interpolation")
    plt.grid(True)

    plt.show()