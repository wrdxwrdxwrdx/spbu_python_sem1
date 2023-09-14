from math import acos, pi


def dot_product(a_vector, b_vector):
    if len(a_vector) != len(b_vector):
        print('vectors must be of the same dimension')
        return
    else:
        return sum([a_vector[i] * b_vector[i] for i in range(len(a_vector))])


def find_length(vector):
    return (sum([i ** 2 for i in vector])) ** 0.5


def find_angle(a_vector, b_vector):
    return acos(dot_product(a_vector, b_vector) / (find_length(a_vector) * find_length(b_vector))) * 180 / pi


def matrix_transposition(matrix):
    width, height = len(matrix[0]), len(matrix)
    return [[matrix[y][x] for y in range(height)] for x in range(width)]


def matrix_sum(a_matrix, b_matrix):
    width, height = len(a_matrix[0]), len(a_matrix)
    return [[a_matrix[y][x] + b_matrix[y][x] for x in range(width)] for y in range(height)]


def matrix_multipy(a_matrix, b_matrix):
    if len(a_matrix) != len(b_matrix[0]) or len(a_matrix[0]) != len(b_matrix):
        print("Please enter correct input (matrix_1 width = matrix_2 height, matrix_1 height = matrix_2 width)")
        return
    a_width, a_height = len(a_matrix[0]), len(a_matrix)
    b_width, b_height = len(b_matrix[0]), len(b_matrix)

    return [[sum([a_matrix[y_a][x_a] * b_matrix[x_a][x_b] for x_a in range(a_width)]) for x_b in range(b_width)] for y_a
            in range(a_height)]


def output_dot_product(input_vector):
    print("\n", *input_vector)
    a_index, b_index = list(
        map(int, input(f"choose indexes of 2 vectors (from 0 to {len(input_vector) - 1}): ").split()))
    print(
        f"\n{input_vector[a_index]} * {input_vector[b_index]} = {dot_product(input_vector[a_index], input_vector[b_index])}")


def output_find_length(input_vector):
    print("\n", *input_vector)
    a_index = int(input(f"choose index of 1 vector (from 0 to {len(input_vector) - 1}): "))
    print(f"\nlength of {input_vector[a_index]} is {find_length(input_vector[a_index])}")


def output_find_angle(input_vector):
    print("\n", *input_vector)
    a_index, b_index = list(
        map(int, input(f"choose indexes of 2 vectors (from 0 to {len(input_vector) - 1}): ").split()))
    print(
        f"\nangle between {input_vector[a_index]} and {input_vector[b_index]} equals to {find_angle(input_vector[a_index], input_vector[b_index])} degrees")


def enter_vector():
    print("\nplease enter your vectors: ")
    input_vector = input('type (x0,y0,z0..) (x1,y1,z1..) ... (xn,yn,zn..): ')
    input_vector = input_vector.split()
    input_vector = [list(map(int, element[1:-1].split(','))) for element in input_vector]
    return input_vector


def show_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))


def enter_matrix(matrix_count):
    input_matrix = []
    for i in range(matrix_count):
        input_matrix.append([])
        row = input()
        while row != "stop":
            input_matrix[-1].append(list(map(int, row.split())))
            row = input()
        if i != matrix_count - 1:
            print("\nnext one\n")

    return input_matrix


def output_matrix_transposition(input_matrix):
    print('\n', *input_matrix)
    a_index = int(input(f"choose index of 1 matrix (from 0 to {len(input_matrix) - 1}): "))
    print(f"\ntransposed matrix:")
    show_matrix(matrix_transposition(input_matrix[a_index]))


def output_matrix_sum(input_matrix):
    print('\n', *input_matrix)
    a_index, b_index = list(
        map(int, input(f"choose indexes of 2 matrices (from 0 to {len(input_matrix) - 1}): ").split()))
    if len(input_matrix[a_index]) != len(input_matrix[b_index]) or len(input_matrix[a_index][0]) != len(
            input_matrix[b_index][0]):
        print("\nPlease enter correct input (matrix sizes should be equal)")
    else:
        print("\nsum of two matrices:")
        show_matrix(matrix_sum(input_matrix[a_index], input_matrix[b_index]))


def output_matrix_multipy(input_matrix):
    print('\n', *input_matrix)
    a_index, b_index = list(
        map(int, input(f"choose indexes of 2 matrices (from 0 to {len(input_matrix) - 1}): ").split()))
    print("\nmultiplication of two matrices:")
    if matrix_multipy(input_matrix[a_index], input_matrix[b_index]):
        show_matrix(matrix_multipy(input_matrix[a_index], input_matrix[b_index]))


if __name__ == "__main__":
    is_running = True

    while is_running:
        print("\nchoose object: \n"
              "\t(1) vector\n"
              "\t(2) matrix")
        answer = int(input("your choice: "))

        # Vectors
        if answer == 1:

            # Vector input
            input_vector = enter_vector()
            is_vector = True
            while is_vector:
                print("\nchoose operation: \n"
                      "\t(1) dot product\n"
                      "\t(2) find length\n"
                      "\t(3) find angle")
                answer = int(input("your choice: "))

                # Dot product

                if answer == 1:
                    output_dot_product(input_vector)

                # Length

                elif answer == 2:
                    output_find_length(input_vector)

                # Angle

                elif answer == 3:
                    output_find_angle(input_vector)

                # Error

                else:
                    print("error")

                user_answer = int(input("\n(1) stop, (2) change object or (3) continue: "))
                if user_answer == 1:
                    is_vector = False
                    is_running = False
                elif user_answer == 2:
                    is_vector = False

        # Matrix

        elif answer == 2:
            matrix_count = int(input("\nenter number of matrices: "))
            print(f"\nenter rows x0 x1 .. xn. To end the entry, write 'stop'\n")

            # Matrix input
            input_matrix = enter_matrix(matrix_count)
            is_matrix = True
            while is_matrix:
                print("\nchoose operation: \n"
                      "\t(1) transposition\n"
                      "\t(2) addition\n"
                      "\t(3) multiplication")
                answer = int(input("your choice: "))

                # Transposition

                if answer == 1:
                    output_matrix_transposition(input_matrix)

                # Addition

                elif answer == 2:
                    output_matrix_sum(input_matrix)

                # Multiplication

                elif answer == 3:
                    output_matrix_multipy(input_matrix)

                else:
                    print("error")

                user_answer = int(input("\n(1) stop, (2) change object or (3) continue: "))
                if user_answer == 1:
                    is_matrix = False
                    is_running = False
                elif user_answer == 2:
                    is_matrix = False
