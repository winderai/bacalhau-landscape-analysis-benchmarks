#!/bin/bash

# fail fast
set -euxo pipefail

# launch job
$HADOOP_HOME/bin/yarn jar word-count/hadoop/wc.jar WordCount ${DATASET_LOCATION} out \
    -D yarn.app.mapreduce.am.resource.memory-mb=32000 \
    -D yarn.app.mapreduce.am.resource.vcores=4 \
    -D mapreduce.map.resource.memory-mb=96000 \
    -D mapreduce.map.resource.vcores=32 \
    -D mapreduce.reduce.resource.memory-mb=96000 \
    -D mapreduce.reduce.resource.vcores=32