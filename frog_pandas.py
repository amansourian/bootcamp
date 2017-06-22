import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# group our data by individual frogs
imp_force_df = df.loc[:, ['ID', 'impact force (mN)']]
grouped = imp_force_df.groupby('ID')

# find mean of the columns
df_mean = grouped.apply(np.mean)

# view the data
print(df_mean)
