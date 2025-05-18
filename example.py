import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(0)
n = 150

# Base DataFrame with one main variable
df_all = pd.DataFrame({
    'V1': np.random.normal(0, 1, n)
})

# Strongly/moderately correlated variables (based on V1)
df_all['V2'] = df_all['V1'] * 0.97 + np.random.normal(0, 1, n)
df_all['V3'] = df_all['V1'] * 0.94 + np.random.normal(0, 1, n)
df_all['V4'] = df_all['V1'] * 0.90 + np.random.normal(0, 1, n)
df_all['V5'] = df_all['V1'] * 0.85 + np.random.normal(0, 1, n)
df_all['V6'] = df_all['V1'] * 0.80 + np.random.normal(0, 1, n)
df_all['V7'] = df_all['V1'] * 0.75 + np.random.normal(0, 1, n)
df_all['V8'] = df_all['V1'] * 0.70 + np.random.normal(0, 1, n)
df_all['V9'] = df_all['V1'] * 0.68 + np.random.normal(0, 1, n)
df_all['V10'] = df_all['V1'] * 0.65 + np.random.normal(0, 1, n)

# Another correlation group (V100, V101, V102)
df_all['V100'] = np.random.normal(0, 1, n)
df_all['V90'] = df_all['V100'] * 0.65 + np.random.normal(0, 1, n)

df_all['V101'] = np.random.normal(0, 1, n)
df_all['V91'] = df_all['V101'] * 0.65 + np.random.normal(0, 1, n)

df_all['V102'] = np.random.normal(0, 1, n)
df_all['V91'] = df_all['V102'] * 0.65 + np.random.normal(0, 1, n)

# List of variable pairs (edges in the graph)
l = [
    ('V1', 'V2'),
    ('V1', 'V3'),
    ('V1', 'V4'),
    ('V3', 'V4'),
    ('V6', 'V4'),
    ('V1', 'V6'),
    ('V5', 'V7'),
    ('V8', 'V9'),
    ('V8', 'V10'),
    ('V8', 'V5'),
    ('V8', 'V6'),
    ('V9', 'V10'),
    ('V6', 'V7'),
    ('V1', 'V10'),
    ('V1', 'V8'),
    ('V90', 'V100'),
    ('V91', 'V101'),
    ('V91', 'V102'),
]

# Call the function to visualize the correlation graph
GraphLation(df_all, l)
