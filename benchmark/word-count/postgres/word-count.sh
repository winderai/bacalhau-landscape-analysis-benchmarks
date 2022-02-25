#!/bin/bash

# fail fast
set -euxo pipefail


sudo -u postgres dropdb --if-exists wordcountdb
sudo -u postgres createdb wordcountdb

sudo -u postgres psql -d wordcountdb -c "CREATE TABLE wordcount(word TEXT);"

wget -P /tmp/ "https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt"

tr " " "\n" < /tmp/wordcount.txt | sudo -u postgres psql -d wordcountdb -c "COPY wordcount FROM stdin (delimiter ' ');"

sudo -u postgres psql -d wordcountdb -c "SELECT word, COUNT(word) 
FROM wordcount 
GROUP BY word 
ORDER BY count DESC 
LIMIT 10;"