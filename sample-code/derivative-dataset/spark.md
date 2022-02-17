- number of partitions?

```
import glob

def func(x):
    import pandas as pd
    df = pd.read_csv(x)
    df_head = df.head(10)
    df_head.to_csv("/dev/null")

rdd = sc.parallelize(glob.glob('data/*.csv'))
rdd.map(lambda file_path: func(file_path)).collect()
```