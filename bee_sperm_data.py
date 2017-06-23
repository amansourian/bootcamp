import numpy as np
import pandas as pd
import bootcamp_utils
import matplotlib.pyplot as plt

import seaborn as sns

"""Use numpy and matplotlib to plot data and use seaborn to format."""

# JB's preferences.
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


# extract data
df_weight = pd.read_csv('data/bee_weight.csv', comment='#')

df_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

# group data
gb_treatment_weight = df_weight.groupby('Treatment')

gb_treatment_sperm = df_sperm.groupby('Treatment')

# separate dataframe into two dataframes for control/pesticide
df_control_weight = df_weight.loc[df_weight['Treatment'] == 'Control', :]
df_pesticide_weight = df_weight.loc[df_weight['Treatment'] == 'Pesticide', :]

df_control_sperm = df_sperm.loc[df_sperm['Treatment'] == 'Control', :]
df_pesticide_sperm = df_sperm.loc[df_sperm['Treatment'] == 'Pesticide', :]


# compute mean weights/sperm of control/pesticide groups !!!
mean_control_weight = df_control_weight.loc[:, 'Weight'].apply(np.mean)
mean_pesticide_weight = df_pesticide_weight.loc[:, 'Weight'].apply(np.mean)

mean_control_sperm = df_control_sperm.loc[:, 'Quality'].apply(np.mean)
mean_pesticide_sperm = df_pesticide_sperm.loc[:, 'Quality'].apply(np.mean)

# # compute median weights/sperm of control/pesticide groups !!!
mean_cont_weight = np.mean(df_weight.loc[df_weight['Treatment']=='Control', 'Weight'])
mean_pest_weight = np.mean(df_weight.loc[df_weight['Treatment']=='Pesticide', 'Weight'])

mean_cont_sperm = np.mean(df_sperm.loc[df_sperm['Treatment']=='Control', 'Quality'])
mean_pest_sperm = np.mean(df_sperm.loc[df_sperm['Treatment']=='Pesticide', 'Quality'])

# print median weight/quality for control/pesticide groups
print('Mean weight for control: ', mean_cont_weight, 'mg')
print('Mean weight for pesticide: ', mean_pest_weight, 'mg')

print('Mean quality for control: ', mean_cont_sperm, 'mg')
print('Mean quality for pesticide: ', mean_pest_sperm, 'mg')

# create and compute bootstrap replicates
# bs_replicate_weight = bootcamp_utils.bs_replicate(df_weight.loc
#                             [:, 'Weight'], func=np.mean)

bs_reps_weight = np.array([bootcamp_utils.bs_replicate
                            (df_weight.loc[:, 'Weight'], func=np.mean)
                            for _ in range(100000)])

# bs_replicate_sperm = bootcamp_utils.bs_replicate(df_sperm.loc[:, 'Quality'].dropna(),
#                                                     func=np.mean) # !!!

bs_reps_sperm = np.array([bootcamp_utils.bs_replicate
                            (df_sperm.loc[:, 'Quality'].dropna(), func=np.mean)
                            for _ in range(100000)])

# compute confidence interval
conf_int_weight = np.percentile(bs_reps_weight, [2.5, 97.5])
print(conf_int_weight)

conf_int_sperm = np.percentile(bs_reps_sperm, [2.5, 97.5])
print(conf_int_sperm) # !!!

# create more bootstrap replicates for plotting
bs_samp_control_weight = np.random.choice(df_control_weight['Weight'],
                            replace=True,
                            size=len(df_control_weight['Weight']))
bs_samp_pesticide_weight = np.random.choice(df_pesticide_weight['Weight'],
                            replace=True,
                            size=len(df_pesticide_weight['Weight']))

bs_samp_control_sperm = np.random.choice(df_control_sperm['Quality'].dropna(),
                            replace=True,
                            size=len(df_control_sperm['Quality'].dropna()))
bs_samp_pesticide_sperm = np.random.choice(df_pesticide_sperm['Quality'].dropna(),
                            replace=True,
                            size=len(df_pesticide_sperm['Quality'].dropna()))


# convert bootstrap sample array to dataframe
df_bs_control_weight = pd.DataFrame(bs_samp_control_weight)
df_bs_pesticide_weight = pd.DataFrame(bs_samp_pesticide_weight)

df_bs_control_sperm = pd.DataFrame(bs_samp_control_sperm)
df_bs_pesticide_sperm = pd.DataFrame(bs_samp_pesticide_sperm)

# rename columns in bootstrap dataframes
df_bs_control_weight.columns = ['bs_Control']
df_bs_pesticide_weight.columns = ['bs_Pesticide']

df_bs_control_sperm.columns = ['bs_Control']
df_bs_pesticide_sperm.columns = ['bs_Pesticide']

# concatenate bootstrap dataframes into one dataframe
df_bs_weight = pd.concat((df_bs_control_weight, df_bs_pesticide_weight),
                            axis=1)

df_bs_sperm = pd.concat((df_bs_control_sperm, df_bs_pesticide_sperm),
                            axis=1)

# 'tidy' our bootstrap data
df_bs_weight = pd.melt(df_bs_weight, var_name='Treatment',
             value_name='Weight').dropna()

df_bs_sperm = pd.melt(df_bs_sperm, var_name='Treatment',
             value_name='Quality').dropna()

# plot ecdf for bootstrap sample
bootcamp_utils.ecdf_plot(df_bs_weight, 'Weight', hue='Treatment', formal=False)

bootcamp_utils.ecdf_plot(df_bs_sperm, 'Quality', hue='Treatment', formal=False)

# plot ecdf for control/pesticide bee weights
bootcamp_utils.ecdf_plot(df_weight, 'Weight', hue='Treatment', formal=False)

bootcamp_utils.ecdf_plot(df_sperm, 'Quality', hue='Treatment', formal=False)

plt.show()
