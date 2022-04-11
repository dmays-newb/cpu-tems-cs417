"""
matrices.py
====================================
Structuring the data for analysis.
"""

import numpy as np


def create_seconds_list(row_count):
    """
    Create a np.array (dim: row_count x 1) of seconds; each entry is 30*row_number
    :param row_count: number of rows in the provided core_temp file
    :return: list of seconds 0 - 30*row_count
    """

    seconds_array = np.zeros((row_count, 1))
    for i in range(0, row_count):
        seconds_array[i] = i*30

    return seconds_array


def create_x(row_count):
    """
    Create an np.array (row_count*1) for a 30 second interval. Ex [[0,30],
        [30, 60], ..., [(row_count-1)*30, row_count*30]]
    :param row_count: number of rows in the input file
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
    Matrices class which contains and constructs from the reading_list:
        x_matrix (second intervals) : example [[0,30], [30, 60]]
        y_matrix (temps) : [61.0, 80.0]
        x_transpose : transposed x_matrix
    """

    def __init__(self, reading_list, row_count):
        """
        Constructs from reading_list all required matrices
        :param reading_list: temperature reading list for a given core
        :param row_count: number of rows in input file
        """
        self.x_matrix = create_x(row_count)
        # print(self.x_matrix)
        self.x_transpose = self.x_matrix.transpose()
        # print(self.x_transpose)
        self.y_matrix = np.array(reading_list)
        # print(self.y_matrix)


