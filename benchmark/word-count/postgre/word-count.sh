#!/bin/bash

# debug
set -x

dropdb wordcountdb
createdb wordcountdb

psql -d wordcountdb -c "CREATE TABLE wordcount(word TEXT);"

wget -P /tmp/ "https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt"

tr " " "\n" < /tmp/wordcount.txt | psql -d wordcountdb -c "COPY wordcount FROM stdin (delimiter ' ');"

# psql -d wordcountdb -c "SELECT * FROM wordcount LIMIT 15;"