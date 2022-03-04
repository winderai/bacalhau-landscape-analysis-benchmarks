# Protocol Labs - Landscape Analysis

## Sample code


|                     | hadoop             | spark              | pandas             | dask               | postgres           | snowflake          |
|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| [word-count](./sample-code/word-count)          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [average-house-price](./sample-code/average-house-price) | :white_check_mark: | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: | :white_check_mark: |
| [derivative-dataset](./sample-code/derivative-dataset)  |                    | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: |                    |

## Benchmark Instructions



1. Create the AWS resources necessary to host your cluster by following the [AWS installation instructions](installation/AWS.md). In this step, you'll set the number of EC2 instances you're going to spin up.
1. Install the various computation frameworks on your hosts by following the instructions, we provide [single-node](installation/SINGLE-NODE.md) and [multi-node](installation/MULTI-NODE.md) setups, depending on the cluster size you'd like to deploy. You need `ssh` to access to the hosts.
1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on the main cluster node.
1. Run the [benchmark](benchmark/README.md) scripts.

## Todo


Benchmarks:

- [x] Build JARs for Hadoop and Spark examples
- [x] run_experiment.py for Hadoop
- [x] run_experiment.py for Spark
- [ ] make sure experiment prepping (init dirs, fetch dataset) is not counted against the benchmarking 
- [ ] Fetch CPU/Memory stats
- [ ] Fetch large dataset
- [ ] Move dataset to S3? or HDFS?
- [ ] disable web UI for clusters?


