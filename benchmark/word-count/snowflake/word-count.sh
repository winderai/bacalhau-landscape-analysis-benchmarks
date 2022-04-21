#!/bin/bash

# fail fast
set -euxo pipefail

# load data into table
/home/ubuntu/bin/snowsql --query "COPY INTO ${DATASET_NAME} FROM '@${SNOW_STAGE}';"

# run query
/home/ubuntu/bin/snowsql --query "SELECT word, COUNT(*) as count
  from (
    select c.value::string as word 
    from "${SNOW_DBNAME}"."${SNOW_SCHEMANAME}"."${DATASET_NAME}", 
          lateral flatten(input=>split(C1, ' ')) c
  )
  group by word
  limit 10;"