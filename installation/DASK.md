# Dask Distributed

## Pre-requisites

First, impersonate hadoopuser (`su - hadoopuser`) to align this setup with Hadoop and Spark installations.

Second, install miniconda (confirm/proceed when prompted). Skip if it's already installed:

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh
echo "eval $(/home/${USER}/miniconda3/bin/conda shell.bash hook)" | tee ~/.bashrc
source ~/.bashrc
```

These instructions assume you've set up `/etc/hosts` (as described in the [Hadoop installation](./HADOOP.md)) and therefore you can reference cluster nodes with `hadoop-master`, `hadoop-slave1`, and so on.
If you're installing Dask without a prior Hadoop setup, please replace those host names with `Private IPv4 addresses` from AWS console (e.g., `172.31.25.80`).

## Install Dask

Install Dask in a conda environment:

```bash
conda create -y -n dask python=3.9
conda activate dask
conda install -y dask==2022.2.0 distributed==2022.2.0 -c conda-forge
pip install requests==2.27.1 aiohttp==3.8.1
pip install --upgrade click==8.0.2 # https://github.com/dask/distributed/issues/6013
```

## Launch cluster

On main node:

```bash
dask-scheduler
```

On each worker node :warning: :

```
dask-worker tcp://hadoop-master:8786
```

Check Dask web UI at `http://<MASTER_PUBLIC_IP>:8787/`. 
Use `Public IPv4 address` from the AWS console.

## Optional: Test Dask Distributed installation

Fire up a Python REPL on main node and run the following snippet:

```python
from dask.distributed import Client

client = Client('hadoop-master:8786')
print(client)

def square(x):
    return x ** 2

def neg(x):
        return -x

A = client.map(square, range(50_000))
B = client.map(neg, A)
total = client.submit(sum, B)
total.result()
```
