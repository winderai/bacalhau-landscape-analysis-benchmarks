#!/bin/bash

# fail fast
set -euxo pipefail


if [ ${DATASET_NAME} = "wordcountTiny" ]; then
    /home/ubuntu/bin/snowsql --query "SELECT word, COUNT(*) as count
      from (
        select c.value::string as word 
        from "${SNOW_DBNAME}"."${SNOW_SCHEMANAME}"."${DATASET_NAME}", 
              lateral flatten(input=>split(C1, ' ')) c
      )
      group by word
      limit 10;"
else
  echo "try again"
fi