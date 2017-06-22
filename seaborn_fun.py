import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

"""Use numpy and matplotlib to plot data and use seaborn to format."""

# JB's preferences.
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

ax = sns.swarmplot(data=df, x='ID', y='impact force (mN)', hue='date')
ax.set_xlabel('')
ax.set_ylabel('Impact Force (mN)')
ax.legend_.remove()

plt.show()
