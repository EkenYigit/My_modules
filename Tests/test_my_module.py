"""
Testing for my_module.py
"""

import My_module as mym
import pytest

def test_times_table():
        """
        Function for testing times_tabel(arg)
        """
        table = mym.times_table(5)
        assert float(table[0,0]) == float(0)
        assert float(table[1,1]) == float(1)
        assert float(table[2,2]) == float(4)
        assert float(table[3,3]) == float(9)
        assert float(table[4,4]) == float(16)
        assert float(table[5,5]) == float(25)
        assert float(table[2,3]) == float(6)
        assert float(table[3,2]) == float(6)

