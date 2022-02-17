# Pandas

Install miniconda (confirm/proceed when prompted):

```
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh
```

Install pandas in a conda environment:

```
eval "$(/home/ubuntu/miniconda3/bin/conda shell.bash hook)"

conda create -y -n pandas python=3.9
conda activate pandas
conda install -y -c conda-forge pandas==1.4.0
```

## Test installation:

Run the following snippet in a `python` REPL:

```
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)

print(myvar)
```