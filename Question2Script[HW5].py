import math
import numpy as np
import matplotlib.pyplot as plt

eager_alpha = 8.12526448 * (10 ** -7)
eager_beta = 2.88591663 * (10 ** -10)
rend_alpha = 2.35555103 * (10 ** -6)
rend_beta = 1.99203990 * (10 ** -10)


def calculateBTARendValues(process_num):
    rend_array = []
    for i in range(11, 26):
        value = (math.log(process_num, 2)) * (rend_alpha + (rend_beta * 8 * (2 ** i)))
        rend_array.append(value)
    return rend_array


def calculateBTAEagerValues(process_num):
    eager_array = []
    for i in range(11):
        value = (math.log(process_num, 2)) * (eager_alpha + (eager_beta * 8 * (2 ** i)))
        eager_array.append(value)
    return eager_array


def calculateSAARendValues(process_num):
    rend_array = []
    for i in range(11, 26):
        value = ((math.log(process_num, 2) + process_num - 1) *
                 rend_alpha) + (2 * ((process_num - 1) / process_num) * 8 * (2 ** i) * rend_beta)
        rend_array.append(value)
    return rend_array


def calculateSAAEagerValues(process_num):
    eager_array = []
    for i in range(11):
        value = ((math.log(process_num, 2) + process_num - 1) *
                 eager_alpha) + (2 * ((process_num - 1) / process_num) * 8 * (2 ** i) * eager_beta)
        eager_array.append(value)
    return eager_array


def main():
    process_num = 64  # change to 16,32 or 64 as required
    array1 = []
    for i in range(26):
        array1.append(i)

    bta_eager = calculateBTAEagerValues(process_num)
    bta_rend = calculateBTARendValues(process_num)
    array2 = np.concatenate((bta_eager, bta_rend))
    print(array2)

    saa_eager = calculateSAAEagerValues(process_num)
    saa_rend = calculateSAARendValues(process_num)
    array3 = np.concatenate((saa_eager, saa_rend))
    print(array3)

    plt.plot(array1, array2)
    plt.plot(array1, array3)
    plt.xlabel('X axis is i but it should be 2^i. Showing i for better visualization')
    plt.ylabel('Cost')
    plt.title('Binomial Tree & Scatter and Allgather')
    plt.legend(["Binomial Tree", "Scatter and Allgather"])
    plt.show()


main()
