#!/bin/bash

# fail fast
#set -euxo pipefail

# Download dataset
if [ $1 = "wordcountTiny" ]; then
    wget -P /tmp/ https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt
    echo "/tmp/wordcount.txt" > .dataset_location
elif [ $1 = "worcountLarge" ]; then
    tar -xvf wordcount-1GB.tar.gz -C /tmp/
    mv /tmp/large-textfile.txt /tmp/wordcount-1GB.txt
    echo "/tmp/wordcount-1GB.txt" > .dataset_location
else
    echo "try again"
fi