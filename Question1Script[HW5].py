import numpy as np
from scipy import linalg


def main():
    eager_dbl = np.array([[2000.0, 8.0], [2000.0, 16.0], [2000.0, 32.0], [2000.0, 64.0], [2000.0, 128.0],
                          [2000.0, 256.0], [2000.0, 512.0], [2000.0, 1024.0], [2000.0, 2048.0], [2000.0, 4096.0],
                          [2000.0, 8192.0]])
    rend_dbl = np.array([[2000.0, 16384.0], [2000.0, 32768.0], [2000.0, 65536.0],
                         [2000.0, 131072.0], [2000.0, 262144.0]])
    print(eager_dbl)
    print()
    print(rend_dbl)
    print()
    eager_vec = np.array([[1.724958 * (10 ** -3)], [1.358032 * (10 ** -3)], [1.475811 * (10 ** -3)],
                          [1.701832 * (10 ** -3)], [1.711845 * (10 ** -3)], [1.814842 * (10 ** -3)],
                          [1.940012 * (10 ** -3)], [2.346039 * (10 ** -3)], [3.044128 * (10 ** -3)],
                          [3.879070 * (10 ** -3)], [6.330967 * (10 ** -3)]])
    rend_vec = np.array([[1.071215 * (10 ** -2)], [1.977181 * (10 ** -2)], [3.021812 * (10 ** -2)],
                         [5.530787 * (10 ** -2)], [1.095400 * (10 ** -1)]])

    # eager_vec = eager_vec.T
    # rend_vec = rend_vec.T
    print(eager_vec)
    print()
    print(rend_vec)
    print()

    eager_alpha_beta = np.linalg.lstsq(eager_dbl, eager_vec, rcond=None)
    rend_alpha_beta = np.linalg.lstsq(rend_dbl, rend_vec, rcond=None)
    print(eager_alpha_beta)
    print(rend_alpha_beta)


main()
