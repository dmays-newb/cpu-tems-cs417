"""
output.py
====================================
The module for creating output .txt files.
"""


def create_function_string(coefs):
    """
    INSERT DOC HERE
    :param coefs:
    :return: function string
    """
    coef1 = f"{coefs[0]:.4f}"
    coef0 = f"{coefs[1]:.4f}"
    function = "{c0:>10} +{c1:>10}x".format(c0=coef0, c1 = coef1)

    return function


def create_outfile(coef_list, core, algorithm):
    """
    INSERT DOC HERE
    :param arr:
    :param core:
    :param algorithm:
    :return: VOID
    """

    file_name = algorithm + "-core-" + str(core) + ".txt"
    out = open(file_name, "w")
    time_tracker = 0
    for element in coef_list:
        start = str(time_tracker*30) + " <= x <"
        end = str(time_tracker*30+30)
        y = "y_" + str(time_tracker)
        function = create_function_string(element)
        # print(element) # Debug output
        line = "{s:>15}{e:>8}; {y:<10}={f:>25}; {a}".format(s = start, e = end, y = y, f = function, a = algorithm)
        out.write(line)
        time_tracker += 1
        out.write('\n')
    out.close()
