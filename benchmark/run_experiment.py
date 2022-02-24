"""
This script assumes a runtime environment
with all pre-requistes preinstalled (conda activate benchmark)
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
            cmd = ["python", "word-count/dask/word-count.py"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "pandas":
            cmd = ["python", "word-count/pandas/word-count.py"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "postgre":
            cmd = ["bash", "word-count/postgre/word-count.sh"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "hadoop":
            cmd = ["bash", "word-count/hadoop/run.sh"]
            s = EasyProcess(cmd).call().stderr
            print(s)
        elif args.framework == "spark":
            cmd = ["bash", "word-count/spark/run.sh"]
            call = EasyProcess(cmd).call()
            s = call.stderr
            print(s)
            s = call.stdout
            print(s)

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
