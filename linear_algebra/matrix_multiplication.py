import matplotlib.pyplot as plt


def fill_matrix(M, dimension, current):
    # fills matrix via 3x+1 conjecture
    _current = current
    for i in range(0, dimension):
        row = []
        for j in range(0, dimension):
            if _current == 1:
                _current = current
            elif _current % 2 == 0:
                _current = _current / 2
            else:
                _current = 3 * _current + 1
            row.append(_current)

        M.append(row)


def fill_vector(V, size, current):
    _current = current
    for i in range(0, size):
        if _current == 1:
            _current = current
        elif _current % 2 == 0:
            _current = _current / 2
        else:
            _current = 3 * _current + 1
        V.append(_current)


def flatten_matrix(M):
    result = []
    for i in range(0, len(M)):
        result += M[i]

    return result

def flatten_for_column_graph(M):
    result = []
    for i in range(0, len(M)):
        # result += M[i]
        result.append(M[i])

    return result

def flatten_for_row_graph(M):
    result = []
    for i in range(0, len(M)):
        col = []
        for j in range(0, len(M[0])):
            col.append(M[j][i])
        result.append(col)

    return result


def print_matrix(M):
    print("\nMatrix: ")
    for i in range(0, len(M)):
        for j in range(0, len(M[0])):
            print(str(M[i][j]) + ", ", end='')
        print()


def print_vector(V):
    print("\nVector: ")
    for i in range(0, len(V)):
        print(str(V[i]) + ", ", end="")
    print()


def draw_graph(y_label, x_label, _values, _interval):
    x_range = []

    for i in range(0, len(_values)):
        x_range.append(i * _interval)

    plt.figure(figsize=(13, 9))
    plt.plot(x_range, _values)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.xlim(left=0)
    plt.gca().spines['bottom'].set_position('zero')
    plt.show()


def draw_graphs(y_labels, x_labels, _values, _time_interval):
    total_row_count = len(_values)
    graph_index = 1
    _time_range = []

    for i in range(0, len(_values)):
        current_values = _values[i]

        for j in range(0, len(current_values)):
            _time_range.append(j * _time_interval)

        plt.rcParams["figure.figsize"] = (10, 10)
        plt.subplot(total_row_count * 100 + 10 + graph_index)
        plt.plot(_time_range, current_values)
        plt.ylabel(y_labels[i])
        plt.xlabel(x_labels[i])
        plt.xlim(left=0)
        plt.gca().spines['bottom'].set_position('zero')

        _time_range = []
        graph_index += 1

    plt.show()


def multiply_matrix(M1, M2):
    # https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm

    if len(M1[0]) != len(M2):
        print("First matrix column count should be equal to second matrix row count! "
              "We need a corresponding row of B for every column of A. Because we will calculate the sum of the multiptilcation of these corresponding elements. A(i,k) * B(k,j)")
        return

    product = []
    for i in range(0, len(M1)):
        row = []

        for j in range(0, len(M2[0])):
            sum = 0
            for k in range(0, len(M1[0])):
                sum += M1[i][k] * M2[k][j]

            row.append(sum)

        product.append(row)
    return product

def multiply_matrix(M1, M2):
    # https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm

    if len(M1[0]) != len(M2):
        print("First matrix column count should be equal to second matrix row count! "
              "We need a corresponding row of B for every column of A. Because we will calculate the sum of the multiptilcation of these corresponding elements. A(i,k) * B(k,j)")
        return

    product = []
    for i in range(0, len(M1)):
        row = []

        for j in range(0, len(M2[0])):
            sum = 0
            for k in range(0, len(M1[0])):
                sum += M1[i][k] * M2[k][j]

            row.append(sum)

        product.append(row)
    return product


M1 = []
M2 = []
fill_matrix(M1, 5, 27)
fill_matrix(M2, 5, 27)
print_matrix(M1)
print_matrix(M2)
product = multiply_matrix(M1, M2)
print_matrix(product)
draw_graphs(['', '', ''], ['', '', ''], [flatten_for_column_graph(M1), flatten_for_row_graph(M2), flatten_matrix(product)], 1)
#draw_graph('', '', flatten_matrix(M1), 1)
#draw_graph('', '', flatten_matrix(product), 1)
V1 = []
fill_vector(V1, 5, 27)
print_vector(V1)
