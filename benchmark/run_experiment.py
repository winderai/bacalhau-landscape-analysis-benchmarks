import os
import argparse
from pathlib import Path
import time

import mlflow
from easyprocess import EasyProcess

def main(args):
    # experiment tracking
    mlflow.set_tracking_uri("file:{}/mlflow-files".format(str(Path.home())))
    mlflow.set_experiment(args.experiment_name)
    
    with mlflow.start_run(run_name=args.framework) as parent_run:
        if args.framework == "dask":
            cmd = ["python", "word-count/dask/word-count.py"]
        elif args.framework == "pandas":
            cmd = ["python", "word-count/pandas/word-count.py"]
        elif args.framework == "postgres":
            print("Postgres...")
            cmd = ["bash", "word-count/postgres/word-count.sh"]
        elif args.framework == "hadoop":
            cmd = ["bash", "word-count/hadoop/run.sh"]
        elif args.framework == "spark":
            cmd = ["bash", "word-count/spark/run.sh"]
        elif args.framework == "snowflake":
            print("Snowflake...")
            cmd = ["bash", "word-count/snowflake/word-count.sh"]
        else:
            raise Exception("Framework {} is not supported. Please try again.".format(args.framework))
        
        t0 = time.time()
        call = EasyProcess(cmd).call()
        t1 = time.time()
        mlflow.log_metric("running_time", t1 - t0)
        mlflow.log_metric("start_time", t0)
        mlflow.log_metric("end_time", t1)
        mlflow.log_parameter("dataset_name", os.getenv['DATASET_NAME'])
        
        print("STDERR:")
        s = call.stderr
        print(s)
        print("STDOUT:")
        s = call.stdout
        print(s)

    print("DONE")

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