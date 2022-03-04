#!/bin/bash

# fail fast
set -euxo pipefail

# Download dataset
wget -P /tmp/ https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt

# Push dataset to HDFS
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/hadoopuser
$HADOOP_HOME/bin/hdfs dfs -put -f /tmp/wordcount.txt

# clean up output dir
#rm -rf /tmp/out
$HADOOP_HOME/bin/hdfs dfs -rm -r out

# launch job
# $HADOOP_HOME/bin/hadoop jar wc.jar WordCount /tmp/wordcount.txt /tmp/out
$HADOOP_HOME/bin/yarn jar word-count/hadoop/wc.jar WordCount /user/hadoopuser/wordcount.txt out
