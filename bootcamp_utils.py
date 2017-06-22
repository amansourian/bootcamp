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


def ecdf_plot(data, value, hue=None, formal=False, buff=0.1, min_x=None, max_x=None,
              ax=None):
    """
    Generate `x` and `y` values for plotting an ECDF.

    Parameters
    ----------
    df : Pandas DataFrame
        Tidy DataFrame with data sets to be plotted.
    value : column name of DataFrame
        Name of column that contains data to make ECDF with.
    hue : column name of DataFrame
        Name of column that identifies labels of data. A seperate
        ECDF is plotted for each unique entry.
    formal : bool, default False
        If True, generate `x` and `y` values for formal ECDF.
        Otherwise, generate `x` and `y` values for "dot" style ECDF.
    buff : float, default 0.1
        How long the tails at y = 0 and y = 1 should extend as a
        fraction of the total range of the data. Ignored if
        `formal` is False.
    min_x : float, default None
        Minimum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    max_x : float, default None
        Maximum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise makes a new
        figure/axes.

    Returns
    -------
    output : matplotlib Axes
        Axes object containg ECDFs.
    """

    # Set up axes
    if ax is None:
        fig, ax = plt.subplots(1, 1)
        ax.set_xlabel(str(value))
        ax.set_ylabel('ECDF')

    if hue is None:
        x, y = ecdf(df[value], formal=formal, buff=buff, min_x=min_x, max_x=max_x)

        # Make plots
        if formal:
            _ = ax.plot(x, y)
        else:
            _ = ax.plot(x, y, marker='.', linestyle='none')
    else:
        gb = df.groupby(hue)
        ecdfs = gb[value].apply(ecdf, formal=formal, buff=buff, min_x=min_x, max_x=max_x)

        # Make plots
        if formal:
            for i, xy in ecdfs.iteritems():
                _ = ax.plot(*xy)
        else:
            for i, xy in ecdfs.iteritems():
                _ = ax.plot(*xy, marker='.', linestyle='none')

        # Add legend
        ax.legend(ecdfs.index, loc=0)

    return ax

ax = ecdf_plot(df, 'impact force (mN)', hue='ID')
