import math
import matplotlib.pyplot as plt

short_intra_node_alpha = 8.3 * (10 ** -7)
short_intra_node_beta = 2.083333 * (10 ** - 9)
short_inter_node_alpha = 2.265647 * (10 ** -6)
short_inter_node_beta = 7.420381 * (10 ** -10)

eager_intra_node_alpha = 1.2 * (10 ** -6)
eager_intra_node_beta = 1.041667 * (10 ** -9)
eager_inter_node_alpha = 6.951053 * (10 ** -6)
eager_inter_node_beta = 1.330323 * (10 ** -9)

rend_intra_node_alpha = 2.5 * (10 ** -6)
rend_intra_node_beta = 1.612903 * (10 ** -10)
rend_inter_node_alpha = 4.043622 * (10 ** -6)
rend_inter_node_beta = 1.282775 * (10 ** -9)
rend_injection_bandwidth = 6.6 * (10 ** 9)

array_for_all = []


def model_for_all(s_step_inter_node, s_size_inter_node, e_step_inter_node, e_size_inter_node, r_step_inter_node,
                  r_size_inter_node, ppn, s_step_intra_node, s_size_intra_node, e_step_intra_node, e_size_intra_node,
                  r_step_intra_node, r_size_intra_node):
    modelled_value = (s_step_inter_node * short_inter_node_alpha) + (s_size_inter_node * short_inter_node_beta) + \
                     (s_step_intra_node * short_intra_node_alpha) + (s_size_intra_node * short_intra_node_beta) + \
                     (e_step_inter_node * eager_inter_node_alpha) + (e_size_inter_node * eager_inter_node_beta) + \
                     (e_step_intra_node * eager_intra_node_alpha) + (e_size_intra_node * eager_intra_node_beta) + \
                     (r_step_inter_node * rend_inter_node_alpha) + (
                             (r_size_inter_node * ppn) / rend_injection_bandwidth) + \
                     (r_step_intra_node * rend_intra_node_alpha) + (r_size_intra_node * rend_intra_node_beta)
    array_for_all.append(modelled_value)


def BRUCK(ppn, num_nodes):
    short_step_inter_node = 0
    short_size_inter_node = 0
    eager_step_inter_node = 0
    eager_size_inter_node = 0
    rend_step_inter_node = 0
    rend_size_inter_node = 0
    totalProcesses = ppn * num_nodes

    inter_node_steps = int(math.log(totalProcesses, 2))
    for x in range(inter_node_steps):
        value = 2 ** x
        if value < 62:
            short_step_inter_node = short_step_inter_node + 1
            short_size_inter_node = short_size_inter_node + value
        elif (value >= 62) and (value < 1000):
            eager_step_inter_node = eager_step_inter_node + 1
            eager_size_inter_node = eager_size_inter_node + value
        elif value >= 1000:
            rend_step_inter_node = rend_step_inter_node + 1
            rend_size_inter_node = rend_size_inter_node + value

    short_step_intra_node = 0
    short_size_intra_node = 0
    eager_step_intra_node = 0
    eager_size_intra_node = 0
    rend_step_intra_node = 0
    rend_size_intra_node = 0

    model_for_all(short_step_inter_node, short_size_inter_node, eager_step_inter_node, eager_size_inter_node,
                  rend_step_inter_node, rend_size_inter_node, ppn, short_step_intra_node, short_size_intra_node,
                  eager_step_intra_node, eager_size_intra_node, rend_step_intra_node, rend_size_intra_node)


def INF(ppn, num_nodes):
    short_step_inter_node = 0
    short_size_inter_node = 0
    eager_step_inter_node = 0
    eager_size_inter_node = 0
    rend_step_inter_node = 0
    rend_size_inter_node = 0

    inter_node_steps = int(math.log(num_nodes, 2))
    for x in range(inter_node_steps):
        value = 2 ** x
        if value < 62:
            short_step_inter_node = short_step_inter_node + 1
            short_size_inter_node = short_size_inter_node + value
        elif (value >= 62) and (value < 1000):
            eager_step_inter_node = eager_step_inter_node + 1
            eager_size_inter_node = eager_size_inter_node + value
        elif value >= 1000:
            rend_step_inter_node = rend_step_inter_node + 1
            rend_size_inter_node = rend_size_inter_node + value

    short_step_intra_node = 0
    short_size_intra_node = 0
    eager_step_intra_node = 0
    eager_size_intra_node = 0
    rend_step_intra_node = 0
    rend_size_intra_node = 0

    intra_node_steps = inter_node_steps + int(math.log(ppn, 2))
    for x in range(inter_node_steps, intra_node_steps):
        value = 2 ** x
        if value < 62:
            short_step_intra_node = short_step_intra_node + 1
            short_size_intra_node = short_size_intra_node + value
        elif (value >= 62) and (value < 1000):
            eager_step_intra_node = eager_step_intra_node + 1
            eager_size_intra_node = eager_size_intra_node + value
        elif value >= 1000:
            rend_step_intra_node = rend_step_intra_node + 1
            rend_size_intra_node = rend_size_intra_node + value
    model_for_all(short_step_inter_node, short_size_inter_node, eager_step_inter_node, eager_size_inter_node,
                  rend_step_inter_node, rend_size_inter_node, ppn, short_step_intra_node, short_size_intra_node,
                  eager_step_intra_node, eager_size_intra_node, rend_step_intra_node, rend_size_intra_node)


def NAP(ppn, num_nodes):
    short_step_inter_node = 0
    short_size_inter_node = 0
    eager_step_inter_node = 0
    eager_size_inter_node = 0
    rend_step_inter_node = 0
    rend_size_inter_node = 0

    inter_node_steps = int(math.log(num_nodes, ppn))
    for x in range(inter_node_steps):
        value = ppn ** (x + 1)
        if value < 62:
            short_step_inter_node = short_step_inter_node + 1
            short_size_inter_node = short_size_inter_node + value
        elif (value >= 62) and (value < 1000):
            eager_step_inter_node = eager_step_inter_node + 1
            eager_size_inter_node = eager_size_inter_node + value
        elif value >= 1000:
            rend_step_inter_node = rend_step_inter_node + 1
            rend_size_inter_node = rend_size_inter_node + value

    short_step_intra_node = 0
    short_size_intra_node = 0
    eager_step_intra_node = 0
    eager_size_intra_node = 0
    rend_step_intra_node = 0
    rend_size_intra_node = 0

    intra_node_steps = int(math.log(ppn, 2)) * (inter_node_steps + 1)
    for x in range(intra_node_steps):
        value = 2 ** x
        if value < 62:
            short_step_intra_node = short_step_intra_node + 1
            short_size_intra_node = short_size_intra_node + value
        elif (value >= 62) and (value < 1000):
            eager_step_intra_node = eager_step_intra_node + 1
            eager_size_intra_node = eager_size_intra_node + value
        elif value >= 1000:
            rend_step_intra_node = rend_step_intra_node + 1
            rend_size_intra_node = rend_size_intra_node + value

    model_for_all(short_step_inter_node, short_size_inter_node, eager_step_inter_node, eager_size_inter_node,
                  rend_step_inter_node, rend_size_inter_node, ppn, short_step_intra_node, short_size_intra_node,
                  eager_step_intra_node, eager_size_intra_node, rend_step_intra_node, rend_size_intra_node)


def main():
    array = [4, 16]
    for i in array:
        for j in range(3):
            k = i ** (j + 1)
            NAP(i, k)
    arr2 = [None] * len(array_for_all)
    for i in range(0, len(array_for_all)):
        arr2[i] = array_for_all[i]
    array_for_all.clear()

    array = [4, 16]
    for i in array:
        for j in range(3):
            k = i ** (j + 1)
            INF(i, k)
    arr3 = [None] * len(array_for_all)
    for i in range(0, len(array_for_all)):
        arr3[i] = array_for_all[i]
    array_for_all.clear()

    array = [4, 16]
    for i in array:
        for j in range(3):
            k = i ** (j + 1)
            BRUCK(i, k)
    arr4 = [None] * len(array_for_all)
    for i in range(0, len(array_for_all)):
        arr4[i] = array_for_all[i]
    array_for_all.clear()

    array = [4, 16]
    string_array = []
    for i in array:
        for j in range(3):
            k = i ** (j + 1)
            string_array.append(str(i) + " & " + str(k))

    print(arr2)
    print(arr3)
    print(arr4)

    plt.plot(string_array, arr2)
    plt.plot(string_array, arr3)
    plt.plot(string_array, arr4)
    plt.xlabel('PPN and Nodes')
    plt.ylabel('Time')
    plt.title('NAP, INF & BRUCK')
    plt.legend(["NAP", "INF", "BRUCK"])
    plt.show()


main()
