#!/bin/bash

# fail fast
set -euxo pipefail

# load data into table
sudo -u postgres psql -d ${DB_NAME} -c "COPY ${DATASET_NAME} FROM '${DATASET_LOCATION}' (delimiter '~');"

# run query
sudo -u postgres psql -d ${DB_NAME} -c "SELECT word, COUNT(word)
FROM ( SELECT unnest(string_to_array(word, ' ')) AS word FROM ${DATASET_NAME} ) AS word
GROUP BY word 
LIMIT 10;"