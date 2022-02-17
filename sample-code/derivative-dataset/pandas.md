- not parallel
- auto-schema inference

```
import glob
import pandas as pd

for file_path in glob.glob('data/*.csv'):
    print(file_path)
    df = pd.read_csv(file_path)
    df_head = df.head(10)
    df_head.to_csv("/dev/null")
```