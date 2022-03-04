# Spark 3.2.1 (without HDFS)

This is a [standalone deploy mode](https://spark.apache.org/docs/latest/spark-standalone.html
), it simply consists of a couple of launch scripts.

## Pre-requisite

Install Java 8 (if not already installed):

```bash
sudo apt -y update
sudo apt install -y openjdk-8-jdk-headless
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
```

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

Check master's web UI at `http://<MASTER_HOST_PUBLIC_IP>:8080/`

## Launch Spark slave(s)

```bash
$SPARK_HOME/sbin/start-worker.sh spark://<MASTER_PRIVATE_IP_DNS_NAME>:7077
```

Retrieve `<MASTER_PRIVATE_IP_DNS_NAME>` from AWS console or via aws-cli. It should look similar to `ip-172-31-15-62.eu-central-1.compute.internal`.

## Test installation

Run the following from within the spark directory:

```bash
$SPARK_HOME/bin/spark-submit \
    --master spark://<MASTER_PRIVATE_IP_DNS_NAME>:7077 \
    --deploy-mode client \
    --class org.apache.spark.examples.SparkPi examples/jars/spark-examples_2.12-3.2.1.jar \
    1000
```