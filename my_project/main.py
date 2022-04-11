"""
main.py
====================================
The core module of my example project.
"""

import sys
import numpy as np
from matrices import Matrices
from linear import interpolate_list
from leastsquares import least_squares_approx
from input import (parse_raw_temps)
from output import (create_outfile)


def main():
    """
    Lines 35-37 borrowed from T.Kennedy @ https://github.com/cstkennedy/Python-Workshop/wiki/Python-Workshop-3-NumPy
    Coordinates execution of all modules.
    """

    input_temps = sys.argv[1]
    num_lines = sum(1 for line in open(input_temps))
    # print(num_lines)
    time = []
    readings_core_0 = []
    readings_core_1 = []
    readings_core_2 = []
    readings_core_3 = []

    core_readings_list = [readings_core_0,
                          readings_core_1,
                          readings_core_2,
                          readings_core_3]

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            time.append(temps_as_floats[0])
            for count, core in enumerate(core_readings_list):
                core.append(temps_as_floats[1][count])

    for core_num in range(0, 4):
        # Construct required matrices for given core temp readings
        core_matrices = Matrices(core_readings_list[core_num], num_lines)

        # Perform approx/interp algorithms and output to files
        least_squares_coefs = least_squares_approx(core_matrices)
        interpolation_coef_list = interpolate_list(core_matrices)
        create_outfile(least_squares_coefs, core_num, "least-squares-approx")
        create_outfile(interpolation_coef_list, core_num, "interpolation")


if __name__ == "__main__":

    main()
