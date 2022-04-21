#!/bin/bash

# fail fast
set -euxo pipefail


sudo -u postgres psql -d ${DB_NAME} -c "SELECT word, COUNT(word) 
FROM ${DATASET_NAME} 
GROUP BY word 
LIMIT 10;"