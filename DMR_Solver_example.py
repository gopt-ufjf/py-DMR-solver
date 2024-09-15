import numpy as np
from DMR_Solver import dmr_solver


def fnc(x: np.ndarray) -> np.ndarray:
    # Example of usage
    # - Variables
    k = x[0]
    y = x[1]
    w = x[2]
    z = x[3]
    # - Equations
    return np.array([
        k * np.sin(2*w) + y * np.sin(w) - 2 * z,
        k * np.sin(w) - z,
        k**2 * np.cos(2*w) + k*y*np.cos(w),
        2*k + y - 24
    ])


if __name__ == "__main__":
    # Step-1: Define the initial value of variables.
    X0 = np.array([5, 6, 1, 1], dtype=float)

    # Parameters
    TOL = 0.001  # DMR Solver tolerance
    H = 0.000001  # Derivation step
    ITER_MAX = 30  # Maximum of iterations

    # Calling DMR Solver
    (x, iter, exit_flag, jac) = dmr_solver(fnc, X0, TOL, H, ITER_MAX)

    # Solution
    k = x[0]
    y = x[1]
    w = x[2]
    z = x[3]
    print("Solution obtained in {} iterations.\n".format(iter))
    print("k:",k)
    print("y:",y)
    print("w:",w)
    print("z:",z)