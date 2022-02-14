# Spark (without HDFS)

https://spark.apache.org/docs/latest/spark-standalone.html

```
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz
```

```
sudo apt -y update
sudo apt install -y openjdk-8-jdk-headless
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
```

```
./sbin/start-master.sh
```

Check: http://3.69.47.28:8080/

```
./sbin/start-worker.sh spark://ip-172-31-15-62.eu-central-1.compute.internal:7077
```


## Test

```
./bin/spark-submit \
    --master spark://ip-172-31-15-62.eu-central-1.compute.internal:7077 \
    --deploy-mode client \
    --class org.apache.spark.examples.SparkPi examples/jars/spark-examples_2.12-3.2.1.jar \
    1000
```