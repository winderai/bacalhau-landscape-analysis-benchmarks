# Protocol Labs - Landscape Analysis

## Sample code

1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on your machine.
1. Install the [single-node setup](./installation/SINGLE-NODE.md) shipped with this repo.
1. Install `jupyter lab` in your base environment
1. Run `cd sample-code && jupyter lab --ip=0.0.0.0`

|                     | hadoop             | spark              | pandas             | dask               | postgres           | snowflake          |
|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| [word-count](./sample-code/word-count)          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [average-house-price](./sample-code/average-house-price) | :white_check_mark: | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: | :white_check_mark: |
| [derivative-dataset](./sample-code/derivative-dataset)  |                    | :white_check_mark: | :white_check_mark: |                    | :white_check_mark: |                    |

## Benchmark Instructions



1. [Create the AWS resources](installation/AWS.md) to host your cluster. In this step, you'll set the number of EC2 instances you're going to spin up.
1. Clone this repo `git clone https://gitlab.com/WinderAI/protocol-labs/sample-code-benchmark.git` on the main cluster node.
1. Install the various computation frameworks on your hosts by following the instructions, we provide [single-node](installation/SINGLE-NODE.md) and [multi-node](installation/MULTI-NODE.md) setups, depending on the cluster size you'd like to deploy. You need `ssh` to access to the hosts.
1. [Install an AWS CloudWatch agent](installation/CLOUDWATCH.md) on each host.
1. Run the [benchmark](benchmark/README.md) scripts.
1. Fetch CloudWatch metrics