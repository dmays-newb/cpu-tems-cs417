"""
leastsquares.py
====================================
Module for least squares approximation
"""

import numpy as np


def backsolver(matrix_XTX, matrix_XTY):
    """
    Heavily borrowed by T.Kennedy @ "https://github.com/cstkennedy/Python-Workshop/wiki/Python-Workshop-3-NumPy"
    Supports solve_matrix function
    Completes backsolving step of Gaussian Elimination
    Modifieds matrix_XTY to contain the coefficients of the approximation function
    :param matrix_XTX: np.array of Xtranspose*X
    :param matrix_XTY: np.array of Xtranspose*Y
    :return: VOID
    """

    num_rows, _ = matrix_XTX.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            s = matrix_XTX[j, i]
            matrix_XTX[j, i] -= (s * matrix_XTX[i, i])
            matrix_XTY[j] -= (s * matrix_XTY[i])



def solve_matrix(matrix_XTX, matrix_XTY):
    """
    Heavily borrowed by T.Kennedy @ "https://github.com/cstkennedy/Python-Workshop/wiki/Python-Workshop-3-NumPy"
    Supporting function for least_squares_approx()
    Performs pivot, scale, and eliminate steps of Gaussian Elimination
    :param matrix_XTX: np.array of Xtranspose*X
    :param matrix_XTY: np.array of Xtranspose*Y
    :return: np.array::float solution_vector
    """

    num_rows, num_columns = matrix_XTX.shape

    for i in range(0, num_rows):
        # pivot
        largest_idx = i
        current_col = i
        for j in range(i + 1, num_rows):

            if matrix_XTX[largest_idx, i] < matrix_XTX[j, current_col]:
                largest_idx = j

        if largest_idx != current_col:
            matrix_XTX[[i, largest_idx], :] = matrix_XTX[[largest_idx, i], :]
            matrix_XTY[[i, largest_idx]] = matrix_XTY[[largest_idx, i]]

        # scale
        scaling_factor = matrix_XTX[i, i]
        matrix_XTX[i, :] /= scaling_factor
        matrix_XTY[i] /= scaling_factor

        # eliminate
        for row_i in range(i + 1, num_rows):
            scaler = matrix_XTX[row_i][i]
            matrix_XTX[row_i] = matrix_XTX[row_i] - scaler * matrix_XTX[i]
            matrix_XTY[row_i] = matrix_XTY[row_i] - scaler * matrix_XTY[i]

    backsolver(matrix_XTX, matrix_XTY)
    # print(matrix_XTX)
    # print(matrix_XTY)


def least_squares_approx(matrices):
    """
    Coordinates least squares approximation.
    :param matrices: matrices class object containing all temps and time intervals
    :return: np.array of coeffiecients (1x2 matrix)
    """

    matrix_X = matrices.x_matrix
    matrix_XT = matrices.x_transpose
    matrix_Y = matrices.y_matrix
    matrix_XTX = matrix_XT @ matrix_X
    matrix_XTY = matrix_XT @ matrix_Y
    # print(matrix_XTX)
    # print(matrix_XTY)

    solve_matrix(matrix_XTX, matrix_XTY)
    # print(matrix_XTY)

    temp = matrix_XTY[0]
    matrix_XTY[0] = matrix_XTY[1]
    matrix_XTY[1] = temp
    formatted_matrix = np.zeros((1,2))
    formatted_matrix[0] = matrix_XTY
    return formatted_matrix