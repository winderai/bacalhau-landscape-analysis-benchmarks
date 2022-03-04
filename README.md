# sample-code-benchmark

## Sample code

- word-count
- average-house-price
- derivative-dataset

## Benchmark Instructions


1. Clone this repo.
1. Create the AWS resources necessary to host your cluster by following the [AWS installation instructions](installation/AWS.md). In this step, you'll set the number of EC2 instances you're going to spin up.
1. Install the various computation frameworks on your hosts by following the instructions, we provide [single-node](installation/SINGLE-NODE.md) and [multi-node](installation/MULTI-NODE.md) setups, depending on the cluster size you'd like to deploy. You need `ssh` to access to the hosts.
1. Run [benchmark](benchmark/README.md).

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


