import pandas as pd

file_url = "https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt"
df = pd.read_csv(file_url, header=None)


df["mytext_new"] = df[0].str.lower().str.replace('[^\w\s]','')
 
 
new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
 
new_df.columns = ['Word', 'Frequency'] 
 
new_df