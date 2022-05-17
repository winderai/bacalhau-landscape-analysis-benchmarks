# Protocol Labs - Landscape Analysis

> This project was created by [Winder.ai, an ML consultancy](https://winder.ai/), and funded by [Protocol Labs](https://protocol.ai/).

This repository contains (1) a collection of working code samples to demonstrate a variety of use cases for different computing frameworks; (2) a benchmark facility to compare running time and resource utilization of different computing frameworks.

## Sample code

|                     | hadoop             | spark              | pandas             | dask               | postgres           | snowflake          |
|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| [word-count](./sample-code/word-count)          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [average-house-price](./sample-code/average-house-price) | :white_check_mark: | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: | :white_check_mark: |
| [derivative-dataset](./sample-code/derivative-dataset)  |                    | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: |                    |


1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on your machine.
1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step, you'll set the number of EC2 instances you're going to spin up.
1. Install the [single-node setup](./installation/SINGLE-NODE.md) shipped with this repo.
1. Install `jupyter lab` in your base environment.
1. Launch `cd sample-code && jupyter lab --ip=0.0.0.0` to run the sample notebooks in `sample-code/`.

## Benchmark instructions

1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step, you'll set the number of EC2 instances you're going to spin up.
1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on the main cluster node.
1. Install the various computation frameworks on your hosts by following the instructions, we provide [Single-node](installation/SINGLE-NODE.md) and [Multi-node](installation/MULTI-NODE.md) setups, depending on the cluster size you'd like to deploy. You need `ssh` to access to the hosts.
1. [Install an AWS CloudWatch agent](installation/CLOUDWATCH.md) on each host.
1. [Run the benchmark](benchmark/README.md) scripts.
1. Fetch CloudWatch metrics