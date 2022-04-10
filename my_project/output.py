"""
output.py
====================================
The module for creating output .txt files.
"""


def create_outfile(arr, core, algorithm):
    """
    INSERT DOC HERE
    """

    file_name = "core_" + str(core) + ".txt"
    out = open(file_name, "w")
    time_tracker = 0
    for element in arr:
        # print(element) # Debug output
        line = str(time_tracker*30) + "     <= x <     " +\
               str(time_tracker*30+30) + ";" +\
               "      y_" + str(time_tracker) + "     =     " +\
               str(element) + ";   " + algorithm
        out.write(line)
        time_tracker += 1
        out.write('\n')
    out.close()
