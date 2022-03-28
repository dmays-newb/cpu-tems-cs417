"""
output.py
====================================
The module for creating output .txt files.
"""

import sys

def create_outfile(arr, core):

    file_name = "core_" + str(core) + ".txt"
    out = open(file_name, "w")
    for element in arr:
        # print(element)
        out.write(str(element))
        out.write('\n')
    out.close()