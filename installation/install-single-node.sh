#!/bin/bash

# fail fast
set -euxo pipefail

# Install conda
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh
eval "$(/home/ubuntu/miniconda3/bin/conda shell.bash hook)"

# Install pandas
conda create -y -n pandas python=3.9
conda activate pandas
conda install -y -c conda-forge pandas==1.4.0
pip install mlflow==1.23.1 EasyProcess==1.1

# Install Dask
conda create -y -n dask python=3.9
conda activate dask
conda install -y dask==2022.2.0 distributed==2022.2.0 -c conda-forge
pip install requests==2.27.1 aiohttp==3.8.1 mlflow==1.23.1 EasyProcess==1.1

# Create base conda env
conda activate base
pip install mlflow==1.23.1 EasyProcess==1.1

# Install postgres
cd ~
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql-14 postgresql-contrib

# Install Hadoop
cd ~
sudo apt -y update
sudo apt install -y ssh pdsh
sudo apt install -y openjdk-8-jdk-headless
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz &>/dev/null

# Install Spark
cd ~
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz &>/dev/null


# Add env var to bash config
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' >> ~/.bashrc 
echo 'export PATH=${JAVA_HOME}/bin:${PATH}' >> ~/.bashrc 
echo 'export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar' >> ~/.bashrc 
echo "export HADOOP_HOME=/home/${USER}/hadoop-3.3.1" >> ~/.bashrc 
echo "export SPARK_HOME=/home/${USER}/spark-3.2.1-bin-hadoop3.2" >> ~/.bashrc 
echo "eval $(/home/${USER}/miniconda3/bin/conda shell.bash hook)" >> ~/.bashrc

# SnowflakeSQL (client)
cd ~
curl -O https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowsql-1.2.21-linux_x86_64.bash
bash snowsql-1.2.21-linux_x86_64.bash
mkdir -p ~/.snowsql
echo "[connections]
accountname = ${SNOW_ACCOUNTNAME}
username = ${SNOW_USERNAME}
password = ${SNOW_PWD}
region = ${SNOW_REGION}
dbname = ${SNOW_DBNAME}
schemaname = ${SNOW_SCHEMANAME}
warehousename = ${SNOW_WAREHOUSENAME}

[variables]

[options]
auto_completion = True
log_file = ~/snowsql_rt.log
log_level = DEBUG
timing = True
output_format = psql
key_bindings = vi
repository_base_url = https://sfc-repo.snowflakecomputing.com/snowsql" > ~/.snowsql/config
chmod 700 ~/.snowsql/config

# Done!
echo "************************************"
echo "Congrats! You've installed them all."
echo "************************************"