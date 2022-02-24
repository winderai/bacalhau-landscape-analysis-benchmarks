# Benchmark


## Install pre-requistes

1) sign up for Databricks Community Edition
2) er signing up, run `databricks configure` to create a credentials file for MLflow, specifying https://community.cloud.databricks.com as the host.

https://www.mlflow.org/docs/latest/quickstart.html#log-to-databricks-community-edition

https://community.cloud.databricks.com/?o=2203001738482424#mlflow/experiments



```
# Install miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh

# Create conda env
eval "$(/home/ubuntu/miniconda3/bin/conda shell.bash hook)"
conda create -y -n benchmark python=3.9
conda activate benchmark

# Install pandas and Dask
conda install -y pandas==1.4.0 dask==2022.2.0 distributed==2022.2.0 -c conda-forge
pip install requests==2.27.1 aiohttp==3.8.1 mlflow==1.23.1 EasyProcess==1.1 databricks-cli

# Install Postgre
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql-14 postgresql-contrib
sudo -i -u postgres


# Install JDK for Hadoop/Spark
conda install -c conda-forge openjdk==8.0.312
echo $JAVA_HOME



# Download Hadoop
sudo apt -y update
sudo apt install -y ssh
sudo apt-get install -y pdsh
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz
export HADOOP_HOME="/home/ubuntu/hadoop-3.3.1"


# Download Spark
cd ~
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz
export SPARK_HOME=/home/ubuntu/spark-3.2.1-bin-hadoop3.2


# Launch Hadoop / Spark?
```

## Dask

Launch `run_experiment.py` from within the main node.

```
python run_experiment.py --experiment_name /test --framework postgre
```