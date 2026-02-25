import pandas as pd
import numpy as np

nrows = 1000
np.random.seed(0)

# Generate a random 5-digit integer for each row, without replacement
to_sample_from = np.arange(10000, 99999)
df = pd.DataFrame({ 'id': np.random.choice(to_sample_from, nrows, replace=False) })

# Generate a random age between 18 and 65 for each row
df['age'] = np.random.randint(18, 65, nrows)

# Generate a random integer between 0 and 2 for each row
df['n_doses'] = np.random.randint(0, 3, nrows)

# Randomly insert NaN values in the 'n_doses' column
n_nan = 88
nan_indices = np.random.choice(df.index, n_nan, replace=False)
df.loc[nan_indices, 'n_doses'] = np.nan

# write this to file
df.to_csv('data/debug_data.csv', index=False)
