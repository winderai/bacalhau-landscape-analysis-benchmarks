import os
import pandas as pd

file_url = os.environ["DATASET_LOCATION"]

df = pd.read_csv(file_url, header=None)
# count words
new_df = (
    df[0]
    .str
    .split(expand=True)
    .stack()
    .value_counts()
)

print(new_df.head())
