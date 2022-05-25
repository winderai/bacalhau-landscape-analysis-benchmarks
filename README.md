# [Protocol Labs] Compute Over Data Landscape Analysis - Landscape Analysis

> This project was created by [Winder.ai, an ML consultancy](https://winder.ai/), and funded by [Protocol Labs](https://protocol.ai/).

This repository contains a detailed analysis of the current state of general purpose computation frameworks and a series of sample demos and benchmarks.

We've intentionally reviewd a wide range of heterogeneous frameworks to provide you with both a broad overview and to capture nuances between frameworks.
Thus, next to big data tools like [Apache Hadoop](https://hadoop.apache.org/) and [Apache Spark](https://spark.apache.org/), we've reviewed databases such as [Postgres](https://www.postgresql.org/) and [Snowflake](https://www.snowflake.com/). 
Note the latter is a proprietary SaaS warehouse product, despite the amount of insights on its internal processing is limited we've included it for its blazoned performance.
We counldn't not wink to the pythonic data analysis world, so we've also included very popular anaylsis tools like [Pandas](https://pandas.pydata.org/) and it's parallel/distributed brother [Dask](https://dask.org/).




Hereby you find: (1) a collection of working code examples to demonstrate a variety of use cases for different computing frameworks, the table below illustrates the coverage; (2) scripts and instructions to benchmark running time and resource utilization of different computing frameworks. Please see the instructions below.


## Sample code

We provide working examples for [embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) workloads that could be computed next to data.

|                     | hadoop             | spark              | pandas             | dask               | postgres           | snowflake          |
|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| [Word count](./sample-code/word-count)          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Average house price](./sample-code/average-house-price) | :white_check_mark: | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: | :white_check_mark: |
| [Derivative dataset (e.g. `head -n 10 <file.txt>`)](./sample-code/derivative-dataset)  |                    | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: |                    |

### Instructions

1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on your machine.
1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step you shall spin up one single EC2 instance.
1. Install the [single-node setup](./installation/SINGLE-NODE.md) shipped with this repo.
1. Install `jupyter lab` in your base environment.
1. Launch `cd sample-code && jupyter lab --ip=0.0.0.0` to run the sample notebooks in `sample-code/`.

## Benchmark instructions

### Instructions

1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step, you'll set the number of EC2 instances you're going to spin up.
1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on the main cluster node.
1. Install the various computation frameworks on your hosts by following the instructions, we provide [Single-node](installation/SINGLE-NODE.md) and [Multi-node](installation/MULTI-NODE.md) setups, depending on the cluster size you'd like to deploy. You need `ssh` to access to the hosts.
1. [Install an AWS CloudWatch agent](installation/CLOUDWATCH.md) on each host.
1. [Run the benchmark](benchmark/README.md) scripts.
1. Fetch CloudWatch metrics

---

For further details on this repository please reach out to Enrico (enrico@winder.ai) or Phil (phil@winder.ai).
