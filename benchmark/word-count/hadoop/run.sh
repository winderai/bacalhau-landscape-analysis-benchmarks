#!/bin/bash

# fail fast
set -euxo pipefail

# launch job
$HADOOP_HOME/bin/yarn jar word-count/hadoop/wc.jar WordCount ${DATASET_LOCATION} out