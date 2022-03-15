#!/bin/bash

# fail fast
set -euxo pipefail

if [ ${DATASET_NAME} = "wordcountTiny" ]; then
    sudo -u postgres psql -d ${DB_NAME} -c "SELECT word, COUNT(word) 
    FROM ${DATASET_NAME} 
    GROUP BY word 
    LIMIT 10;"
else
  echo "try again"
fi