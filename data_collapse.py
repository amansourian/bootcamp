import numpy as np

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(palette=colors, rc={'axes.labelsize': 16})

"""
Plotting fold change and theoretical fold change in order to
demonstrate data collapse.
"""

# Load in data sets.
q18a = np.loadtxt('data/q18a_lac.csv', skiprows=3, delimiter=',')
q18m = np.loadtxt('data/q18m_lac.csv', skiprows=3, delimiter=',')
wt = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')

# Slice out IPTG (mM) and fold change.
q18a_iptg = q18a[:,0]
q18a_fold_change = q18a[:,1]

q18m_iptg = q18m[:,0]
q18m_fold_change = q18m[:,1]

wt_iptg = wt[:,0]
wt_fold_change = wt[:,1]

# Set up plot figures.
fig, ax = plt.subplots(1, 1)
ax.set_xlabel('$x$ = IPTG Concentration')
ax.set_ylabel('$f(x)$ = Fold Change')
ax.set_xscale('log')

# Plot folt IPTG and fold change.
_ = ax.plot(q18a_iptg, q18a_fold_change, marker='.', linestyle='none',
            label='Q18A')
_ = ax.plot(q18m_iptg, q18m_fold_change, marker='.', linestyle='none',
            label='Q18M')
_ = ax.plot(wt_iptg, wt_fold_change, marker='.', linestyle='none',
            label='WT')

# Write function for computing theoretical fold change.
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):

    fc = (1 + (RK*(1+c/KdA)**2) / ((1+c/KdA)**2 + Kswitch*(1+c/KdI)**2))**(-1)
    return fc


# Assign variable for logspace with parameters corresponding to data sets.
x = np.logspace(-6.3,1.6, num=100)

# Assign variables to given R/K ratios.
q18a_rk = 16.56
q18m_rk = 1332
wt_rk = 141.5

# Plot theoretical fold change.
_ = ax.plot(x, fold_change(x, q18a_rk), color=colors[0], alpha=.5)
_ = ax.plot(x, fold_change(x, q18m_rk), color=colors[1], alpha=.5)
_ = ax.plot(x, fold_change(x, wt_rk), color=colors[2], alpha=.5)

ax.legend()

plt.show()
