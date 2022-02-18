```python
import pandas as pd

file_path = "./data/wordcount.txt"

df = pd.read_csv(file_path, header=None)

df["mytext_new"] = df[0].str.lower().str.replace('[^\w\s]','')
  
new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
 
new_df.columns = ['Word', 'Frequency'] 
 
print(new_df)
```