import bioinfo_dicts as bd

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
