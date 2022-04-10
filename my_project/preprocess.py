"""
preprocess.py
====================================
Structuring the data for analysis
"""

import numpy as np


def create_seconds_list(row_count):
    """
    INSERT DOC HERE
    :param row_count:
    :return: list of seconds 0 - 30*row_count
    """

    seconds_array = np.zeros((row_count, 1))
    for i in range(0, row_count):
        seconds_array[i] = i*30

    return seconds_array


def create_x(row_count):
    """
    INSERT DOC HERE
    :param row_count:
    :return: two-dimensional np.array (matrix) -> X0 and X1
    """

    x_zero = np.ones(row_count)
    x_one = create_seconds_list(row_count)
    x_matrix = np.column_stack((x_zero, x_one))
    # print(x_matrix)
    # print(x_matrix[0][1])
    return x_matrix


class Matrices:
    """
    INSERT DOC HERE
    """

    def __init__(self, reading_list, row_count):
        self.x_matrix = create_x(row_count)
        # print(self.x_matrix)
        self.x_transpose = self.x_matrix.transpose()
        # print(self.x_transpose)
        self.y_matrix = np.array(reading_list)
        # print(self.y_matrix)


