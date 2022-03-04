import argparse

import mlflow
from easyprocess import EasyProcess

def main(args):
    # experiment tracking
    mlflow.set_tracking_uri("file:./mlflow-files")
    mlflow.set_experiment(args.experiment_name)
    
    with mlflow.start_run(run_name=args.framework) as parent_run:
        if args.framework == "dask":
            cmd = ["python", "word-count/dask/word-count.py"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "pandas":
            mlflow.log_param("param1", 1111)
            mlflow.log_metric("foo", 222)
            cmd = ["python", "word-count/pandas/word-count.py"]
            s = EasyProcess(cmd).call().stdout
            print(s)
        elif args.framework == "postgres":
            print("Postgres...")
            cmd = ["bash", "word-count/postgres/word-count.sh"]
            call = EasyProcess(cmd).call()
            s = call.stderr
            print(s)
            s = call.stdout
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
        else:
            raise Exception("Framework {} is not supported.".format(args.framework))
        
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
