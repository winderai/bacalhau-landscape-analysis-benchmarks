#!/bin/bash

# fail fast
set -euxo pipefail

# Download dataset
if [ $1 = "wordcount-tiny" ]; then
    wget -P /tmp/ https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt
    echo "/tmp/wordcount.txt" > .dataset_location
else
  echo "try again"
fi