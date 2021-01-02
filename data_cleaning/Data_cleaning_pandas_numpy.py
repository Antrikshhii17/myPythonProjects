import pandas as pd
import numpy as np


# Read csv into dataframe
file = r'C:\Users\antriksh.chourasia\PycharmProjects\data_cleaning\leba_gpl2.csv'
df = pd.read_csv(file, index_col=None)

# Transformation - Find all the NaN value indices and their count
column1 = np.where(np.isnan(df['value']))
print(column1)
print('Count =', np.count_nonzero(column1))

# Fill all the NaN values with zero
column2 = np.where(np.isnan(df['value']), 0, df['value'])
print(column2)

# Let's check again if we have any NaN. Result should be- array[]
column3 = np.where(np.isnan(column2))
print(column3)

# Now let's merge this column back into the dataframe
df['value'] = column2
print(df)

# Extract Absolute period from Description column
column4 = df['Model Code'].apply(lambda v: v[v.find("ASS.")+6:v.find('/MID')])
print(column4)

# Now we create a new column 'AbsolutePeriod' and fill it with the column4 values
df['AbsolutePeriod'] = column4
print(df)

# Once we verify the transformations are done correctly, we can create a csv file
df.to_csv(r'C:\Users\antriksh.chourasia\PycharmProjects\data_cleaning\newFile.csv')
