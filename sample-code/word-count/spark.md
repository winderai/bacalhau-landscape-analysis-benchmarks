# Spark word count


```
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz

```



```
./bin/spark-submit \
    --master spark://ip-172-31-15-62.eu-central-1.compute.internal:7077 \
    --deploy-mode client \
    --class org.apache.spark.examples.SparkPi examples/jars/spark-examples_2.12-3.2.1.jar \
    1000
```



```
wget https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/trees.csv


./bin/spark-submit --master local --class org.apache.spark.examples.JavaWordCount examples/jars/spark-examples_2.12-3.2.1.jar \
    trees.csv
```