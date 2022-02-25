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

# Install Dask
conda create -y -n dask python=3.9
conda activate dask
conda install -y dask==2022.2.0 distributed==2022.2.0 -c conda-forge
pip install requests aiohttp

#
conda activate base

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
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export PATH=${JAVA_HOME}/bin:${PATH}
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
tar -xvf hadoop-3.3.1.tar.gz &>/dev/null
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
export HADOOP_HOME="/home/ubuntu/hadoop-3.3.1"

# Install Spark
cd ~
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
tar -xvf spark-3.2.1-bin-hadoop3.2.tgz &>/dev/null
export SPARK_HOME=/home/ubuntu/spark-3.2.1-bin-hadoop3.2