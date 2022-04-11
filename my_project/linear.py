"""
linear.py
====================================
Module for piecewise linear interpolation.
"""

import numpy as np


def interpolate_list(matrices):
    """
    Creates list of interpolation functions for given matrices
    :param matrices: matrices class object containing all temps and time intervals
    :return: numpy array of 2 coefficients (tuples); shape: (num_input_rows - 1) x 2
    """

    Y = matrices.y_matrix
    row_count = Y.shape[0]

    X = np.hsplit(matrices.x_matrix, 2)
    X = X[1].reshape(row_count, 1)
    # print("X: ", X) # Check that X is correct

    # print(row_count) # Check row count against list
    coefficient_list = np.zeros((row_count-1, 2))

    a = 0.
    b = 0.
    denom = 0.

    for i in range(0, row_count-1):
        denom = (X[i] - X[i+1])
        a = (Y[i] - Y[i+1]) / denom
        b = ((Y[i+1]*X[i]) - (Y[i]*X[i+1])) / denom
        coefficient_list[i][0] = a
        coefficient_list[i][1] = b

    # print(coefficient_list) # check for correct coefficients

    return coefficient_list

