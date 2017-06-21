import os

"""
Using 'with' block to read sequence and store as single string with no gaps.
"""

with open('~git/bootcamp/data/salmonella_spi1_region.fna') as f:
    f_str = f.readlines[1:20]
