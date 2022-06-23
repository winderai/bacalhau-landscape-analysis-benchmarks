# [Protocol Labs] Compute Over Data Landscape Analysis - Bacalhau

> This project was created by [Winder.ai, an ML consultancy](https://winder.ai/), and funded by [Protocol Labs](https://protocol.ai/).

This repository contains a detailed analysis of the current state of general-purpose computation frameworks and a series of sample demos and benchmarks.

We've intentionally reviewed a wide range of heterogeneous frameworks to provide a broad overview and capture nuances between frameworks.
Thus, next to big data tools like [Apache Hadoop](https://hadoop.apache.org/) and [Apache Spark](https://spark.apache.org/), we've reviewed databases such as [Postgres](https://www.postgresql.org/) and [Snowflake](https://www.snowflake.com/). 
Note the latter is a proprietary SaaS warehouse product, despite the  limited insights on its internal processing we've included it for its blazoned performance.
We couldn't not wink to the pythonic data analysis world, so we've also covered top-rated analysis tools such as [Pandas](https://pandas.pydata.org/) and its parallel/distributed brother [Dask](https://dask.org/).




In this repository you find: 
1. A collection of working code examples to demonstrate a variety of use cases for different computing frameworks, the table below illustrates the coverage.
2. A set of scripts and instructions to benchmark running time and resource utilization of different computing frameworks. Please see the instructions below.

> We provide accompanying slides that summarize this work and report on the benchmarks results - [[link to slides](https://docs.google.com/presentation/d/1wOh-ASGshgc1Ivkoyaz9zGpVGTxX9LDMZQB4-eXOBP4/edit?usp=sharing)].

## Sample code

We provide working examples for [embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) workloads that can be computed next to data.

Take a look at the [`sample-code/`](./sample-code) folder for viewing the demos (no installation needed!). 
If you want to run them live, please follow the instructions below.


|                     | hadoop             | spark              | pandas             | dask               | postgres           | snowflake          |
|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| [Word count](./sample-code/word-count)          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Average house price](./sample-code/average-house-price) | :white_check_mark: | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: | :white_check_mark: |
| [Derivative dataset (i.e. `head -n 10 <file.txt>`)](./sample-code/derivative-dataset)  |                    | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: |                    |

### Instructions

1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on your machine.
1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step you shall spin up one single EC2 instance.
1. Install the [single-node setup](./installation/SINGLE-NODE.md) shipped with this repo.
1. Install `jupyter lab` in your base environment.
1. Launch `cd sample-code && jupyter lab --ip=0.0.0.0` to run the sample notebooks in `sample-code/`.

## Benchmarks

The benchmarks consist of a timed [Word count](https://en.wikipedia.org/wiki/Word_count) job running on all frameworks mentioned above.
Each run is launched one at a time and requires some manual preliminary work (e.g. spin-up cluster).
During the creation of AWS resources you can select the number of nodes you'd like to spawn, can do single or multi-node setups.
The difference is the latter installation is way more cumbersome so take your time.

To facilitate the logging of running time, job parameters and various environment variables, the launch scripts use [MLflow](https://mlflow.org/).
Differently, resource usage (i.e., cpu, memory, disk) is logged via [AWS CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
This means CloudWatch metrics can be fetched from their dashboard starting from 5-10 minutes after the experiment has been completed.
This is to allow the metrics to flow into AWS sink.

Feel free to explore the [`benchmark/`](./benchmark) directory to familiarize yourself with this setup, or follow the instructions below to spawn a cluster and run the benchmarks.

### Instructions

1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step, you'll set the number of EC2 instances you're going to spin up.
1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on the main cluster node.
1. Install the various computation frameworks on your hosts by following the instructions, we provide [Single-node](installation/SINGLE-NODE.md) and [Multi-node](installation/MULTI-NODE.md) setups, depending on the cluster size you'd like to deploy. You need `ssh` to access to the hosts.
1. [Optional] [Install an AWS CloudWatch agent](installation/CLOUDWATCH.md) on each host.
1. [Run the benchmark](benchmark/README.md) scripts.
1. [Optional] Fetch CloudWatch metrics through AWS console.

---

For further details on this repository please reach out to Enrico (enrico@winder.ai) or Phil (phil@winder.ai).
