# Benchmark WIP



Benchmark sequence WIP:

- start cluster
- pull dataset to local stash
- push dataset to most convenient location (eg. hdfs, snowflake stage/table, etc.)
- save timestamp for metrics retrieval `START`
- **timed!: run actual computation (no put print, no write to files, just computation)**
- save timestamp for metrics retrieval `END`
- stop cluster (to allow for other experiments to run)
- fetch metrics from mlflow
- fetch metrics from CloudWatch (wait x minutes)
- [ ] disable web UI for clusters?



Make sure your shell is pointing to the conda base environemnt, if that's not the case just do `source ~/.bashrc`.
Now you can launch `run_experiment.py` from within the main node.
You may need to install the following python packages `pip install mlflow==1.23.1 EasyProcess==1.1`.
If you're in a multi-node setup, run the benchmarks as `hadoopuser` instead of the default `ubuntu` user.

```bash
# preliminary setup
export EXP_NAME=cluster-size-1
export DATASET_NAME=wordcountTiny|wordcountLarge|wordcountXL # use camel-case naming
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
    --experiment_name /${EXP_NAME} \
    --framework pandas

conda activate base
```

## Dask

```bash
conda activate dask

# !Important: start cluster only in multi-node setup
dask-scheduler # On main node
dask-worker tcp://hadoop-master:8786 # On each worker node

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework dask

# stop cluster by killing the related processes, if started before

conda activate base
```

## Postgres

```bash
conda activate base

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# prepare dataset
export DB_NAME=${DATASET_NAME}Db
sudo -u postgres dropdb --if-exists ${DB_NAME}
sudo -u postgres createdb ${DB_NAME}
sudo -u postgres psql -d ${DB_NAME} -c "CREATE TABLE ${DATASET_NAME}(word TEXT);"

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework postgres

# quick check
sudo -u postgres psql -d ${DB_NAME} -c "SELECT * FROM ${DATASET_NAME} LIMIT 10;"
```

## Snowflake

Make you have `SNOW_DBNAME` and `SNOW_SCHEMANAME` properly set up, if not take a look at the [Snowflake installation instructions](../installation/SNOWFLAKE.md#set-environment-variables).
Furthemore, you'll need to a Snowflake stage to host your dataset, please check the [official docs](https://docs.snowflake.com/en/user-guide/data-load-local-file-system.html) to learn how to create one.

```bash
conda activate base

export SNOW_STAGE=<your-snowflake-stage>

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# prepare data
/home/ubuntu/bin/snowsql --query "DROP STAGE IF EXISTS ${SNOW_STAGE};"
/home/ubuntu/bin/snowsql --query "CREATE STAGE ${SNOW_STAGE};"
/home/ubuntu/bin/snowsql --query "PUT file://${DATASET_LOCATION} '@${SNOW_STAGE}';"
/home/ubuntu/bin/snowsql --query "DROP TABLE IF EXISTS ${DATASET_NAME};"
/home/ubuntu/bin/snowsql --query "CREATE TABLE ${DATASET_NAME}(C1 STRING);"

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework snowflake

# quick check
/home/ubuntu/bin/snowsql --query "SELECT * FROM ${DATASET_NAME} LIMIT 10;"
```


## Hadoop

```bash
conda activate base

## !Important: impersonate `hadoopuser` only in multi-node setup
##su - hadoopuser

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# !Important: start cluster only in multi-node setup
# Run on main node
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# check cluster status
$HADOOP_HOME/bin/hdfs dfsadmin -report # in single-node setup this will ouput "The fs class is: org.apache.hadoop.fs.LocalFileSystem"

# !Important: only in multi-node setup
# Push dataset to HDFS
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put -f ${DATASET_LOCATION} /user/hadoopuser
export DATASET_LOCATION=$(echo "/user/hadoopuser/$(basename ${DATASET_LOCATION})")

# clean up output dir
$HADOOP_HOME/bin/hdfs dfs -rm -r out

# TODO may need to install conda here in multi-node

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework hadoop

$HADOOP_HOME/bin/hadoop fs -cat ./out/part-r-00000 | head

# stop cluster, if started before
# Run on main node
$HADOOP_HOME/sbin/stop-dfs.sh
$HADOOP_HOME/sbin/stop-yarn.sh
```

## Spark

```bash
conda activate base

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# !Important: only in multi-node setup
# start cluster
$SPARK_HOME/sbin/start-master.sh # launch on master node
$SPARK_HOME/sbin/start-worker.sh spark://hadoop-master:7077 # launch on each worker node

# !Important: only in multi-node setup
# distribute dataset across cluster
 # run this for each slave node, replace the node indexing accordingly (e.g. hadoop-slave2, hadoop-slave3, etc.)
#scp ${DATASET_LOCATION} hadoopuser@hadoop-slave1:${DATASET_LOCATION}

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework spark

# run on master node
$SPARK_HOME/sbin/stop-master.sh
# run on each worker node
$SPARK_HOME/sbin/stop-worker.sh
```

# Multi-node cluster

## Dask

```bash
## !Important: impersonate `hadoopuser` only in multi-node setup
su - hadoopuser

conda activate dask

# !Important: start cluster only in multi-node setup
dask-scheduler # On main node
dask-worker tcp://hadoop-master:8786 # On each worker node

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework dask

# stop cluster by killing the related processes, if started before

conda activate base
```

## Hadoop

```bash
conda activate base

## !Important: impersonate `hadoopuser` only in multi-node setup
##su - hadoopuser

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# !Important: start cluster only in multi-node setup
# Run on main node
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# check cluster status
$HADOOP_HOME/bin/hdfs dfsadmin -report # in single-node setup this will ouput "The fs class is: org.apache.hadoop.fs.LocalFileSystem"

# !Important: only in multi-node setup
# Push dataset to HDFS
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put -f ${DATASET_LOCATION} /user/hadoopuser
export DATASET_LOCATION=$(echo "/user/hadoopuser/$(basename ${DATASET_LOCATION})")

# clean up output dir
$HADOOP_HOME/bin/hdfs dfs -rm -r out

# TODO may need to install conda here in multi-node

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework hadoop

$HADOOP_HOME/bin/hadoop fs -cat ./out/part-r-00000 | head

# stop cluster, if started before
# Run on main node
$HADOOP_HOME/sbin/stop-dfs.sh
$HADOOP_HOME/sbin/stop-yarn.sh
```

## Spark

```bash
conda activate base

# pull data to local dir
bash pull-dataset.sh ${DATASET_NAME}
export DATASET_LOCATION=$(cat .dataset_location)

# !Important: only in multi-node setup
# start cluster
$SPARK_HOME/sbin/start-master.sh # launch on master node
$SPARK_HOME/sbin/start-worker.sh spark://hadoop-master:7077 # launch on each worker node

# !Important: only in multi-node setup
# distribute dataset across cluster
 # run this for each slave node, replace the node indexing accordingly (e.g. hadoop-slave2, hadoop-slave3, etc.)
#scp ${DATASET_LOCATION} hadoopuser@hadoop-slave1:${DATASET_LOCATION}
# TODO copy dataset over each node

python run_experiment.py \
    --experiment_name /${EXP_NAME} \
    --framework spark

# run on master node
$SPARK_HOME/sbin/stop-master.sh
# run on each worker node
$SPARK_HOME/sbin/stop-worker.sh
```

--- 

## CloudWatch metrics

```
export AWS_PROFILE=<your-aws-profile>

python cloudwatch.py \
    --host_ip ip-172-31-12-99 \
    --aws_region eu-central-1 \
    --start_time 1649948609 \
    --end_time 1649949612 \
    --output_dir "/tmp"
```


`mlflow ui --backend-store-uri ~/mlflow-files --host 0.0.0.0`
