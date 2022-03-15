#!/bin/bash

# fail fast
set -euxo pipefail

# launch job
if [ ${DATASET_NAME} = "wordcountTiny" ]; then
    $HADOOP_HOME/bin/yarn jar word-count/hadoop/wc.jar WordCount ${DATASET_LOCATION} out
else
  echo "try again"
fi