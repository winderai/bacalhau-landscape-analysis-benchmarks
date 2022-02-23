import pandas as pd

file_url = "https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt"

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
new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False) 

print(new_df)