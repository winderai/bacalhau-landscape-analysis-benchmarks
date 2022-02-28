# Benchmark





## Dask

Launch `run_experiment.py` from within the main node.

```
conda activate pandas
python run_experiment.py \
    --experiment_name /test \
    --framework pandas
```

```
conda activate dask
python run_experiment.py \
    --experiment_name /test \
    --framework dask
```

postgre:
```
conda activate base
python run_experiment.py \
    --experiment_name /test \
    --framework postgres
```


Hadoop:
```
conda activate base
python run_experiment.py \
    --experiment_name /test \
    --framework hadoop
```

Spark:
```
conda activate base
python run_experiment.py \
    --experiment_name /test \
    --framework spark
```