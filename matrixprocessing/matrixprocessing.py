import copy

class MyError(Exception):
    def __init__(self, error):
        self.error = error


def get_matrix():
    matrix = []
    valid_chars = "0123456789"
    while True:
        try:
            size = input("Enter the size of the matrix:\n> ").split()
            if len(size) != 2 or not all(char.isdigit() for char in size):
                raise MyError('Incorrect input!\nYou should enter the size, like "3 3", "4 4", etc.\n')
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter the matrix:")
    for _ in range(int(size[0])):
        while True:
            try:
                row = input("> ").split()
                if len(row) != int(size[1]) or not all(char.isdigit() for char in row):
                    raise MyError(f'You should enter only {size[1]} numbers in a line!')
                else:
                    matrix.append([float(x) for x in row])
                    break
            except MyError as err:
                print(err)
    return matrix


def add_matrices():
    matrix_a = get_matrix()
    matrix_b = get_matrix()
    if len(matrix_a[0]) != len(matrix_b[0]) or len(matrix_a) != len(matrix_b):
        print("The operation cannot be performed.")
        print("The size of the second matrix must be the same as the size of the first matrix!")
    else:
        print("The result is:")
        for i in range(len(matrix_b)):
            for j in range(len(matrix_b[0])):
                print(int(matrix_a[i][j] + matrix_b[i][j]), end=" ")
            print()


def multiply_constant():
    matrix = get_matrix()
    while True:
        try:
            constant = float(input("Enter a constant:\n> "))
            break
        except ValueError:
            print("Incorrect input! You must enter a number.")
    print("The result is:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j] * constant, end="  ")
        print()


def multiply_matrices():
    int_matrix_a = get_matrix()
    int_matrix_b = get_matrix()
    result = []
    for i in range(len(int_matrix_a)):
        string = []
        for d in range(len(int_matrix_b[0])):
            number = 0
            for k in range(len(int_matrix_a[0])):
                number += int_matrix_a[i][k] * int_matrix_b[k][d]
            string.append(number)
        result.append(string)

    print("The result is:")
    for i in range(len(result)):
        for x in result[i]:
            print(int(x), end=" ")
        print()


def transpose_matrix():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")

    while True:
        try:
            valid_choices = "1234"
            choice_t = input("\nEnter your choice: 1, 2, 3, or 4:\n> ")
            if choice_t not in valid_choices:
                raise MyError("Incorrect input. Please try again.")
            break
        except MyError as error:
            print(error)

    int_matrix = get_matrix()

    result = []
    for i in range(len(int_matrix)):
        string = []
        for d in range(len(int_matrix[0])):
            number = 0
            for k in range(1):
                number += int_matrix[d][i]


            string.append(number)
        result.append(string)

    print("The result is:")
    if choice_t == "1":
        for i in range(len(result)):
            for x in result[i]:
                print(int(x), end=" ")
            print()

    elif choice_t == "2":
        for c in range(len(result)):
            result[c].reverse()
        result.reverse()
        for i in range(len(result)):
            for x in result[i]:
                print(int(x), end=" ")
            print()

    elif choice_t == "3":
        for c in range(len(int_matrix)):
            int_matrix[c].reverse()
        for i in range(len(int_matrix)):
            for x in int_matrix[i]:
                print(int(x), end=" ")
            print()

    elif choice_t == "4":
        int_matrix.reverse()
        for i in range(len(int_matrix)):
            for x in int_matrix[i]:
                print(int(x), end=" ")
            print()


def calculate_determinant(i_m):
    result = 0
    sign_1 = 1
    if len(i_m) == 1:
        result += i_m[0][0]
    elif len(i_m) == 2:
        result += i_m[0][0] * i_m[1][1] - i_m[1][0] * i_m[0][1]
    elif len(i_m) == 3:
        result += i_m[0][0] * (i_m[1][1] * i_m[2][2] - i_m[2][1] * i_m[1][2]) - i_m[0][1] * (
            i_m[1][0] * i_m[2][2] - i_m[2][0] * i_m[1][2]) + i_m[0][2] * (i_m[1][0] * i_m[2][1] - i_m[2][0] * i_m[1][1])
    else:
        for j in range(len(i_m)):
            m_1 = copy.deepcopy(i_m)
            if len(i_m) > 4:
                del m_1[0]
                for i in range(len(m_1)):
                    del m_1[i][j]

            sign = 1
            det = 0
            for b in range(len(m_1)):
                m = copy.deepcopy(m_1)
                del m[0]
                for i in range(len(m)):
                    del m[i][b]

                det += (sign * m_1[0][b]) * (
                        m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] -
                        m[0][2] * m[1][1] * m[2][0] - m[0][0] * m[1][2] * m[2][1] - m[0][1] * m[1][0] * m[2][2])
                if sign == 1:
                    sign = -1
                else:
                    sign = 1
            if len(i_m) > 4:
                result += det * (sign_1 * i_m[0][j])
                if sign_1 == 1:
                    sign_1 = -1
                else:
                    sign_1 = 1
            else:
                result += det
                break
    return result


def minor(a,

 i, j):
    return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]


def cofactor(a, i, j):
    return (-1) ** (i + j) * calculate_determinant(minor(a, i, j))


def inverse_matrix():
    matrix = get_matrix()
    determinant = calculate_determinant(matrix)
    if determinant == 0:
        print("This matrix doesn't have an inverse.")
    else:
        result = []
        for i in range(len(matrix)):
            result_row = []
            for j in range(len(matrix[0])):
                c = cofactor(matrix, i, j)
                result_row.append(c / determinant)
            result.append(result_row)

        print("The result is:")
        for i in range(len(result)):
            for x in result[i]:
                print(x, end="  ")
            print()


def print_menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")


def main():
    while True:
        print_menu()
        choice = input("Your choice:\n> ")
        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            matrix = get_matrix()
            print("The result is:")
            print(calculate_determinant(matrix))
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()