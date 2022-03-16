#!/bin/bash

# fail fast
set -euxo pipefail


# launch job
if [ ${DATASET_NAME} = "wordcountTiny" ]; then
  if [ ${EXP_NAME} = "cluster-size-1" ]; then
    $SPARK_HOME/bin/spark-submit \
      --master local[*] \
      word-count/spark/target/scala-2.12/sparkwordcount_2.12-0.1.jar \
      ${DATASET_LOCATION}
    else
      $SPARK_HOME/bin/spark-submit \
        --master spark://hadoop-master:7077 \
        word-count/spark/target/scala-2.12/sparkwordcount_2.12-0.1.jar \
        ${DATASET_LOCATION}
    fi
else
  echo "try again"
fi
