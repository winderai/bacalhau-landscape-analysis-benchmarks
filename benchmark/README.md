# Benchmark



Benchmark sequence:

- start cluster
- pull dataset to local directory
- push dataset to most convenient location (eg. hdfs, snowflake stage/table, etc.)
- save timestamp for metrics retrieval `START`
- run actual computation (no put print, no write to files, just computation)
- save timestamp for metrics retrieval `END`
- stop cluster (to allow for other experiments to run)
- fetch metrics from mlflow
- fetch metrics from CloudWatch (wait x minutes)


```
pip install mlflow==1.23.1 EasyProcess==1.1
```

Launch `run_experiment.py` from within the main node.

```bash
# preliminary setup
export EXP_NAME=cluster-size-1
export DATASET_NAME=wordcount-tiny|worcount-large|nlp-large
```

## Prerequistes

- ec2 instances running
- single-node or multi node setup
- cloudwatch agent running

## Pandas

```bash
conda activate pandas

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

python run_experiment.py \
    --experiment_name /test \
    --framework pandas

conda activate base
```

## Dask

```bash
conda activate dask

# !Important: start cluster only on multi-node
dask-scheduler # On main node
dask-worker tcp://hadoop-master:8786 # On each worker node

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

python run_experiment.py \
    --experiment_name /test \
    --framework dask

# stop cluster by killing the related processes, if started before

conda activate base
```

## Postgres

```bash
# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# prepare dataset
sudo -u postgres dropdb --if-exists wordcountdb
sudo -u postgres createdb wordcountdb
sudo -u postgres psql -d wordcountdb -c "CREATE TABLE wordcount(word TEXT);"

# load
echo "$(cat ${DATASET_LOCATION})" | tr " " "\n" | sudo -u postgres psql -d wordcountdb -c "COPY wordcount FROM stdin (delimiter ' ');"

conda activate base
python run_experiment.py \
    --experiment_name /test \
    --framework postgres
```

## Hadoop

```bash
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

conda activate base

$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# check cluster status
$HADOOP_HOME/bin/hdfs dfsadmin -report

# Push dataset to HDFS
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put -f ${DATASET_LOCATION}

# clean up output dir
$HADOOP_HOME/bin/hdfs dfs -rm -r out


python run_experiment.py \
    --experiment_name /test \
    --framework hadoop

$HADOOP_HOME/sbin/stop-dfs.sh
$HADOOP_HOME/sbin/stop-yarn.sh
```

## Spark

```bash
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

conda activate base

# launch on master node
$SPARK_HOME/sbin/start-master.sh
# launch on each worker node
$SPARK_HOME/sbin/start-worker.sh spark://hadoop-master:7077

python run_experiment.py \
    --experiment_name /test \
    --framework spark

# launch on master node
$SPARK_HOME/sbin/stop-master.sh
# launch on each worker node
$SPARK_HOME/sbin/stop-worker.sh
```

## Snowflake

```bash
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

conda activate base
python run_experiment.py \
    --experiment_name /test \
    --framework snowflake
```