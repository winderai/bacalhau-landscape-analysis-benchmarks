# Dask Distributed

Install miniconda (confirm/proceed when prompted):

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh
```

Install Dask in a conda environment:

```bash
eval "$(/home/ubuntu/miniconda3/bin/conda shell.bash hook)"
conda create -y -n dask python=3.9
conda activate dask
conda install -y dask==2022.2.0 distributed==2022.2.0 -c conda-forge
pip install requests aiohttp
```

On main node:

```bash
dask-scheduler
```

On each worker node:

```
dask-worker tcp://172.31.11.47:8786
```

## Optional: Test Dask Distributed installation

Run in main node:

```python
from dask.distributed import Client
client = Client('ec2-18-197-25-82.eu-central-1.compute.amazonaws.com:8786')
client

def square(x):
    return x ** 2

def neg(x):
        return -x

A = client.map(square, range(100_000))
B = client.map(neg, A)
total = client.submit(sum, B)
total.result()
```