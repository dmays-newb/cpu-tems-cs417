"""
main.py
====================================
The core module of my example project
"""

import sys
import numpy as np
import preprocess
from leastsquares import least_squares_approx
from input import (parse_raw_temps)
from output import (create_outfile)


def main():
    """
    Lines 29-31 borrowed from T.Kennedy @ https://github.com/cstkennedy/Python-Workshop/wiki/Python-Workshop-3-NumPy
    """

    input_temps = sys.argv[1]
    num_lines = sum(1 for line in open(input_temps))
    # print(num_lines)
    time = []
    readings_core_0 = []
    readings_core_1 = []
    readings_core_2 = []
    readings_core_3 = []

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            time.append(temps_as_floats[0])
            readings_core_0.append(temps_as_floats[1][0])
            # readings_core_1.append(temps_as_floats[1][1])
            # readings_core_2.append(temps_as_floats[1][2])
            # readings_core_3.append(temps_as_floats[1][3])

    core0_matrices = preprocess.Matrices(readings_core_0, num_lines)
    least_squares_fxn = least_squares_approx(core0_matrices)
    print(least_squares_fxn)


    # x_matrix_0 = create_x(readings_core_0, num_lines)
    # x_matrix_1 = create_x(readings_core_1, num_lines)
    # x_matrix_2 = create_x(readings_core_2, num_lines)
    # x_matrix_3 = create_x(readings_core_3, num_lines)

    # create_outfile(readings_core_0, 0, "dummy")
    # create_outfile(readings_core_1, 1, "dummy")
    # create_outfile(readings_core_2, 2, "dummy")
    # create_outfile(readings_core_3, 3, "dummy")


if __name__ == "__main__":

    main()
