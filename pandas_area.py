import pandas as pd


# extract data
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)

# rename columns
df_low.columns = ['low']
df_high.columns = ['high']

# concatenate individual dataFrames
df = pd.concat((df_low, df_high), axis=1)

# 'tidy' our data
df = pd.melt(df, var_name='food density',
             value_name='cross-sectional area (sq micron)').dropna()

df.to_csv('xa_combined.csv', index=False)
