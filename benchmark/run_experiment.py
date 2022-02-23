"""
This script assumes a runtime environment
with all pre-requistes preinstalled
"""

import argparse

import mlflow
from easyprocess import EasyProcess

def main(args):
    # experiment tracking
    mlflow.set_tracking_uri("databricks")
    mlflow.set_experiment(args.experiment_name)
    
    with mlflow.start_run(run_name=args.framework) as parent_run:
        if args.framework == "dask":
            mlflow.log_param("dask", 123123123)
            
            cmd = ["python", "word-count/dask/word-count.py"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "pandas":
            mlflow.log_param("pandas", 123123123)

            mlflow.log_param("tetetetet", 123123123)
            
            cmd = ["python", "word-count/pandas/word-count.py"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "postgre":
            cmd = ["bash", "word-count/postgre/word-count.sh"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "hadoop":
            raise NotImplementedError
        elif args.framework == "spark":
            raise NotImplementedError

        # export JAVA_HOME=...
        # export PATH=${JAVA_HOME}/bin:${PATH}
        # export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
        # export HADOOP_HOME=/Users/enricorotundo/hadoop-3.3.1
        # $HADOOP_HOME/bin/hadoop jar jars/hadoop-wc.jar WordCount ./data ./out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--experiment_name",
        type=str,
        required=True,
        help="The experiment name stored in MLflow. An experiment name must be an absolute path e.g. '/my-experiment'",
    )
    parser.add_argument(
        "--framework",
        type=str,
        required=True,
        help="",
    )
    args = parser.parse_args()
    main(args)
