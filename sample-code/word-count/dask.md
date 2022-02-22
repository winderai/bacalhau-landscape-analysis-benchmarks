# Dask Word Count

Make sure your client has `pip install msgpack==1.0.2  numpy==1.20.3 pandas==1.2.3 requests aiohttp`:

```python
from dask.distributed import Client
client = Client('ec2-18-197-25-82.eu-central-1.compute.amazonaws.com:8786')
import dask.dataframe as dd

file_path = "https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt"

df = dd.read_csv(file_path, header=None)
# count words
new_df = (
    df[0]
    .str
    .split()
    .explode()
    .value_counts()
    .reset_index()
)
new_df.columns = ['Word', 'Frequency']
new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False)

print(new_df.compute())
```


Expected output:

```
          Word  Frequency
0          the         38
1            a         28
2           of         25
3         word         24
4          and         23
..         ...        ...
376       does          1
377  documents          1
378   dividers          1
379    divider          1
380     writer          1

[381 rows x 2 columns]
```