import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import bioinfo_dicts as bd

"""
Module for functions and other utilities written during bootcamp.
"""


def ecdf(data):
    """Compute ECDF function."""
# y_j=(j+1)/n, where n is the number of data points and 0≤j≤n−1.
    x = np.sort(data)
    y = (np.arange(1,len(data) + 1))/len(data)
    return x, y


def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate from data."""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)


def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw bootstrap replicates from 1D data."""
    return np.array([bs_replicate(data, func=func) for _ in range(size)])


def reverse_complement(seq, material = 'DNA'):
    """Compute reverse complement of a sequence."""

    #Initialize the reverse complement
    rev_seq = ''

    for base in seq[::-1]:
        rev_seq += complement_base(base, material = material)

    return rev_seq


def complement_base(base, material = 'DNA'):
    """Returns the Watson-Crick complement of a base."""
    base = base.lower()
    if base == 'a':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'tu':
        return 'A'
    elif base == 'g':
        return 'C'
    else:
        return 'G'


def seq_concat(a, b, **kwargs):
    """Concatenate sequences."""
    seq = a + b

    for key in kwargs:
        seq += kwargs[key]

    return seq


def one_to_three(seq):
    """
    Converts a protein sequence using one letter abbrev.
    to one using three-letter abbrev.
    """

    # Convert the seq to upper case
    seq = seq.upper()

    # Do the conversion, but check that each input AA is valid
    aa_list = []
    for amino_acid in seq:
        if amino_acid not in bd.aa.keys():
            raise RuntimeError(amino_acid + ' is not valid.')
        aa_list += [bd.aa[amino_acid], '-']

    return ''.join(aa_list[:-1])
