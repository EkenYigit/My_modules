"""
Python modules for learning & fastenning
"""
import numpy as np


def times_table(arg):
        """
        Function for printing times table array till [arg]
        """
        arg2 = arg + 1
        table = np.zeros(arg2 ** 2).reshape(arg2, arg2)
        for i in range(1, arg2):
            table[0 , i] = i
            table[i , 0] = i
            for j in range(1, arg2):
                table[i, j] = i * j
        return table

