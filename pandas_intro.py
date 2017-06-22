import pandas as pd

# dictionary to put into a DataFrame
wc_dict = {'Klose': 16,
            'Ronaldo': 15,
            'Muller': 14,
            'Fontaine': 13,
            'Pele': 12,
            'Kocsis': 11,
            'Klinsmann': 11,}

# another dictionary to put into a DataFrame
nation_dict = {'Klose': 'Germany',
                'Ronaldo': 'Brazil',
                'Muller': 'Germany',
                'Fontaine': 'France',
                'Pele': 'Brazil',
                'Kocsis': 'Hungary',
                'Klinsmann': 'Germany',}

# convert dictionary into a Series
s_goals = pd.Series(wc_dict)
s_nation = pd.Series(nation_dict)

df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})
