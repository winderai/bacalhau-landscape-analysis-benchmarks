# sample-code-benchmark

## Sample code

- word-count
- average-house-price
- derivative-dataset

## Benchmark Instructions


1. Clone this repo.
1. Follow the [AWS installation instructions](installation/AWS.md). 
1. Follow benchmark instructions for a [single-node](installation/SINGLE-NODE.md) or [multi-node](installation/MULTI-NODE.md) set up, depending on the cluster size you'd like to deploy. You'll need `ssh` access to the cluster nodes.

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


