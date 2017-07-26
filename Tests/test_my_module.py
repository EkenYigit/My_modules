"""
Testing for my_module.py
"""

import my_module as mym
import pytest

def test_times_table():
	"""
	Function for testing times_tabel(arg)
	"""
	table = mym.times_table(5)
	assert table[0,0] = 0
	assert table[1,1] = 1
        assert table[2,2] = 4
        assert table[3,3] = 9
        assert table[4,4] = 16
        assert table[5,5] = 25
        assert table[2,3] = 6
        assert table[3,2] = 6


