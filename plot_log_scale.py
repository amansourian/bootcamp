import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

# JB's preferences.
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Load in the data.
data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')

# Slice out iptg (mM), gfp, and standard error mean (sem)
iptg = data[:,0]
gfp = data[:,1]
sem = data[:,2]

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('Concentration of IPTG')
ax.set_ylabel('Intensity of GFP')
ax.set_xscale('log')

_ = ax.plot(iptg, gfp, linestyle='none', marker='.')
_ = ax.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.',
                markersize=10)

plt.show()
