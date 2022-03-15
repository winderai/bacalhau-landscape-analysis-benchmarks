#!/bin/bash

# fail fast
set -euxo pipefail


# launch job
if [ ${DATASET_NAME} = "wordcountTiny" ]; then
    $SPARK_HOME/bin/spark-submit \
        --master local \
        word-count/spark/target/scala-2.12/sparkwordcount_2.12-0.1.jar \
        ${DATASET_LOCATION}
else
  echo "try again"
fi