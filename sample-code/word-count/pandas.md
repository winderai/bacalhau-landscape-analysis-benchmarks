# Pandas Word Count

```
conda activate pandas
# start REPL
python 
```

```python
import pandas as pd

# load dataset into DataFrame
file_path = "./data/wordcount.txt"
# each entry contains a text row
df = pd.read_csv(file_path, header=None)

# count words
new_df = (
    df[0]
    .str
    .split(expand=True) # split by ' ' and expand into columns
    .stack() # stack columns vertically -> each entry contains a single word
    .value_counts()
    .reset_index()
)

new_df.columns = ['Word', 'Frequency'] 
new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False) 

print(new_df)
```

Expected output:

```
             Word  Frequency
0             the         38
1               a         28
2              of         25
3            word         24
4             and         23
..            ...        ...
376        tables          1
377   handwriting          1
378       wayside          1
379  particularly          1
380         start          1
```
