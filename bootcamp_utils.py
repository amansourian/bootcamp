"""
Module for functions and other utilities written during bootcamp.
"""

# ECDF function.
def ecdf(data):

# y_j=(j+1)/n, where n is the number of data points and 0≤j≤n−1.
    x = np.sort(data)
    y = (np.arange(1,len(data)) + 1)/len(data)

    return x, y
