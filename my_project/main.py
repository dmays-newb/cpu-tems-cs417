"""
main.py
====================================
The core module of my example project
"""

import sys
# import numpy as np
from input import (parse_raw_temps)
from output import (create_outfile)


def main():
    """
    This main function serves as the driver for the demo. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """

    input_temps = sys.argv[1]
    time = []
    readings_core_0 = []
    readings_core_1 = []
    readings_core_2 = []
    readings_core_3 = []

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            time.append(temps_as_floats[0])
            readings_core_0.append(temps_as_floats[1][0])
            readings_core_1.append(temps_as_floats[1][1])
            readings_core_2.append(temps_as_floats[1][2])
            readings_core_3.append(temps_as_floats[1][3])

    create_outfile(readings_core_0, 0)
    create_outfile(readings_core_1, 1)
    create_outfile(readings_core_2, 2)
    create_outfile(readings_core_3, 3)


if __name__ == "__main__":

    main()
