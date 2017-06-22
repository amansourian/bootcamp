import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

"""
Write a function to find ECDF of a dataset and plot it with sorted data.
"""

# write the ECDF function.
def ecdf(data):

# y_j=(j+1)/n, where n is the number of data points and 0≤j≤n−1.
    x = np.sort(data)
    y = (np.arange(1,len(data)) + 1)/len(data)

    return x, y

# Load in data.
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Generate x and y values for data sets.
ecdf_xa_high = ecdf(xa_high)
ecdf_xa_low = ecdf(xa_low)

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('x = Cross sectional area (sorted)')
ax.set_ylabel('y = ECDF')

_ = ax.plot(ecdf_xa_high[0], ecdf_xa_high[1], marker='.', linestyle='none')
_ = ax.plot(ecdf_xa_low[0], ecdf_xa_low[1], marker='.', linestyle='none')

plt.show()
