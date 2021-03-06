#!/bin/bash

# fail fast
#set -euxo pipefail

# Download dataset
if [ $1 = "wordcountTiny" ]; then
    wget -P /tmp/ https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt
    echo "/tmp/wordcount.txt" > .dataset_location
elif [ $1 = "wordcountLarge" ]; then
    tar -xvf wordcount-1GB.tar.gz -C /tmp/
    mv --no-clobber /tmp/large-textfile.txt /tmp/wordcount-1GB.txt
    echo "/tmp/wordcount-1GB.txt" > .dataset_location
elif [ $1 = "wordcountXL" ]; then
    tar -xvf wordcount-10GB.tar.gz -C /tmp/
    mv --no-clobber /tmp/large-textfile3.txt /tmp/wordcount-10GB.txt
    echo "/tmp/wordcount-10GB.txt" > .dataset_location
else
    echo "try again"
fi