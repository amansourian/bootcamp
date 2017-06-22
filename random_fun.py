import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import bootcamp_utils

"""Use numpy and matplotlib to plot data and use seaborn to format."""

# JB's preferences.
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

mu = 10
sigma = 1

x_rnd = np.random.normal(mu, sigma, size=100000)

# Make ECDF
x, y = bootcamp_utils.ecdf(x_rnd)

# Plot ECDF
fig, ax = plt.subplots(1, 1)
_ = ax.plot(x, y, marker='.', linestyle='none')

plt.show()
