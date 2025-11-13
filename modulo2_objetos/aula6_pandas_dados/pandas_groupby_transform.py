# https://www.geeksforgeeks.org/how-to-reset-index-after-groupby-pandas/


import pandas as pd

# creating dataframe
df = pd.DataFrame({'Subject': ['B', 'C', 'A', 'D', 'C', 'B', 'A'],
                   'Marks': [4, 8, 5, 9, 8, 1, 0]})

# grouping the data on the basis of subject and mean of marks.
df_grouped = df.groupby(['Subject']).mean()

# reset index
df_grouped.reset_index()

# Diferença para o TRANSFORM
df['Marks_mean'] = df.groupby(['Subject']).transform('mean')

