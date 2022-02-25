#!/bin/bash

# fail fast
set -euxo pipefail

# Download dataset
wget -P /tmp/ https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt


# launch job
$SPARK_HOME/bin/spark-submit \
    --master local \
    word-count/spark/target/scala-2.12/sparkwordcount_2.12-0.1.jar \
    /tmp/wordcount.txt