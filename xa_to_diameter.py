import numpy as np

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units.
    """

    # Compute diameter from area
    diameter = 2 * np.sqrt(xa/np.pi)

    return diameter
