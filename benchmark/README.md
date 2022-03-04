# Benchmark

```
pip install mlflow==1.23.1 EasyProcess==1.1
```



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

$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# check cluster status
$HADOOP_HOME/bin/hdfs dfsadmin -report

python run_experiment.py \
    --experiment_name /test \
    --framework hadoop

$HADOOP_HOME/sbin/stop-dfs.sh
$HADOOP_HOME/sbin/stop-yarn.sh
```

Spark:
```
conda activate base
python run_experiment.py \
    --experiment_name /test \
    --framework spark
```