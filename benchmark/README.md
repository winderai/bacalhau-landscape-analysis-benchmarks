# Benchmark


## pre-requistes

### Single node:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
export HADOOP_HOME="/home/ubuntu/hadoop-3.3.1"
export SPARK_HOME=/home/ubuntu/spark-3.2.1-bin-hadoop3.2
```

### multi node:

...

## Dask

Launch `run_experiment.py` from within the main node.

```
python run_experiment.py \
    --experiment_name /test \
    --framework postgre
```