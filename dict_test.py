def seq_concat(a, b, **kwargs):
    """Concatenate sequences."""
    seq = a + b

    for key in kwargs:
        seq += kwargs[key]

    return seq
