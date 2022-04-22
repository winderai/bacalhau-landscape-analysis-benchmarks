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
    .reset_index()
)
new_df.columns = ['Word', 'Frequency'] 
# new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False)

print(new_df.head())


# import gc
# import os
# import pandas as pd

# file_url = os.environ["DATASET_LOCATION"]

# df = pd.read_csv(file_url, header=None)

# df1 = df[0].str.split(expand=True).stack()

# del df
# gc.collect()

# df2 = df1[0]

# del df1
# gc.collect()


# df2 = df2.value_counts()
# df2.columns = ['Word', 'Frequency']
# print(df2.head())

# count words
# new_df = (
#     df[0]
#     .str
#     .split(expand=True)
#     .stack()
#     .value_counts()
#     # .reset_index()
# )
# new_df.columns = ['Word', 'Frequency'] 
# new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False)

# print(new_df.head())