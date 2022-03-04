# Spark 3.2.1 (without HDFS)

This is a [standalone deploy mode](https://spark.apache.org/docs/latest/spark-standalone.html
), it simply consists of a couple of launch scripts.

## Pre-requisite

Install Java 8 (if not already installed with Hadoop):

```bash
sudo apt -y update
sudo apt install -y openjdk-8-jdk-headless
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
```

These instructions assume you've set up `/etc/hosts` (as described in the [Hadoop installation](./HADOOP.md)) and therefore you can reference cluster nodes with `hadoop-master`, `hadoop-slave1`, and so on.
If you're installing Spark without a prior Hadoop setup, please replace those host names with `Public IPv4 DNS` from AWS console (e.g., `ip-172-31-15-62.eu-central-1.compute.internal`).

## Download Spark

```bash
cd ~
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz &>/dev/null
export SPARK_HOME="/home/${USER}/spark-3.2.1-bin-hadoop3.2"
```

## Launch Spark master

```bash
$SPARK_HOME/sbin/start-master.sh
```

Check master's web UI at `http://<MASTER_PUBLIC_IP>:8080/`. Use `Public IPv4 address` from the AWS console.


## Launch Spark slave(s)

```bash
$SPARK_HOME/sbin/start-worker.sh spark://hadoop-master:7077
```


## Test installation

Run the following from within the spark directory:

```bash
$SPARK_HOME/bin/spark-submit \
    --master spark://hadoop-master:7077 \
    --deploy-mode client \
    --class org.apache.spark.examples.SparkPi $SPARK_HOME/examples/jars/spark-examples_2.12-3.2.1.jar \
    10000
```