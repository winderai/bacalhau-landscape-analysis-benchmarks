# Spark word count


```
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz

```



```
wget https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/trees.csv


spark-submit --master local --class org.apache.spark.examples.JavaWordCount examples/jars/spark-examples_2.12-3.2.1.jar \
    trees.csv
```