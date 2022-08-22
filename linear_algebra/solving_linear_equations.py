import random
import fractions
import copy


def random_matrix(row, col, limit):
    matrix = []
    temp = []
    for i in range(row):
        for j in range(col):
            temp.append(fractions.Fraction(random.randint(-limit, limit)))
        matrix.append(temp)
        temp = []
    return matrix


def random_vector(col, limit):
    vector = []
    for i in range(col):
        vector.append(fractions.Fraction(random.randint(-limit, limit)))
    return vector


def print_matrix(matrix):
    print("\nMatrix: ")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]) + ", ", end='')
        print()
    print()


def print_vector(vector):
    print("\nVector: ")
    for i in range(len(vector)):
        print(str(vector[i]) + ", ", end='')
    print()
    print()


def swap_rows(matrix, vector, r1, r2):
    # print(f'#### swapping rows {r1} {r2}')
    last = len(matrix) - 1

    if r1 < 0 | r1 > last | r2 < 0 | r2 > last:
        raise Exception(f'Row number ({r1},{r2}) is out of range (0, {last})!')

    temp = matrix[r1]
    matrix[r1] = matrix[r2]
    matrix[r2] = temp

    temp = vector[r1]
    vector[r1] = vector[r2]
    vector[r2] = temp

    # print_matrix(matrix)
    # print_vector(vector)


def multiply_row(matrix, vector, r1, scalar):
    # print(f'#### multiplying row {r1} with {scalar}')
    if scalar == 0:
        raise Exception('Can not multiply a row with 0!')

    last = len(matrix) - 1
    if r1 < 0 | r1 > last:
        raise Exception(f'Row number ({r1}) is out of range (0, {last})!')

    for i in range(len(matrix[r1])):
        matrix[r1][i] *= scalar

    vector[r1] *= scalar

    # print_matrix(matrix)
    # print_vector(vector)


def add_row_to_another(matrix, vector, r1, r2, scalar):
    # print(f'#### adding {scalar} times row {r2} to row {r1}')
    if scalar == 0:
        raise Exception('Multiplying with 0 has no effect!')

    last = len(matrix) - 1
    if r1 < 0 | r1 > last | r2 < 0 | r2 > last:
        raise Exception(f'Row number ({r1},{r2}) is out of range (0, {last})!')

    for i in range(len(matrix[r2])):
        matrix[r1][i] += scalar * matrix[r2][i]

    vector[r1] += scalar * vector[r2]

    # print_matrix(matrix)
    # print_vector(vector)


def reduce_to_one(matrix, vector, row, col):
    # print(f'#### reducing to 1 ({row}, {col})')
    value = matrix[row][col]

    if value == 1:
        return

    if value == 0:
        for i in range(len(matrix)-1, -1, -1):
            if i != row:
                row_val = matrix[i][col]
                if row_val != 0:
                    add_row_to_another(matrix, vector, row, i, fractions.Fraction(1 - value, row_val))
                    break
    else:
        multiply_row(matrix, vector, row, 1 / value)


def reduce_to_zero(matrix, vector, row, col):
    # print(f'#### reducing to 0 ({row}, {col})')
    value = matrix[row][col]

    if value == 0:
        return

    for i in range(len(matrix)-1, -1, -1):
        if i != row:
            row_val = matrix[i][col]
            if row_val != 0:
                add_row_to_another(matrix, vector, row, i, fractions.Fraction(-value, row_val))
                break


def zero_row(matrix, vector, row):
    for col in range(len(matrix)):
        if matrix[row][col] != 0:
            return False

    if vector[row] == 0:
        print("Infinite solutions!")
    else:
        print("No solution!")

    return True


def reduce_to_identity_matrix(matrix, vector):
    for row in range(0, len(matrix)):
        col = row
        if matrix[row][col] != 1:
            reduce_to_one(matrix, vector, row, col)

        for j in range(len(matrix)):
            if j != row:
                row_val = matrix[j][col]
                if row_val != 0:
                    reduce_to_zero(matrix, vector, j, col)
                    if zero_row(matrix, vector, j):
                        print_matrix(matrix)
                        print_vector(vector)
                        return False
    # print_matrix(matrix)
    # print_vector(vector)
    return True


M_start = []
V_start = []
M_reduced = []
V_reduced = []
no_solution_count = 0
for i in range(100000):
    M_start = random_matrix(5, 5, 10)
    V_start = random_vector(5, 10)

    M_reduced = copy.deepcopy(M_start)
    V_reduced = copy.deepcopy(V_start)
    if not reduce_to_identity_matrix(M_reduced, V_reduced):
        print_matrix(M_start)
        print_vector(V_start)
        print_matrix(M_reduced)
        print_vector(V_reduced)
        no_solution_count += 1
        print("###################################################")


print(f'no_solution_count: {no_solution_count}')



