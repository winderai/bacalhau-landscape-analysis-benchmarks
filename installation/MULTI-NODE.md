# Multi node installation

This set up involves a number of steps run across multiple hosts.
Brew a :coffee: and take your time. 
You'll need to ssh into each node. 
Some commands will be issued on all hosts, others will be only for the master or slave(s), depending on the step.
Rest assured, each instruction makes its target host explicit either in the title or in the description.

For convienence, I'd recommend using [iTerm2's broadcast input](https://christopher.su/notes/mac/iterm-broadcast/) to quickly issue commands across multiple machines.

Proceed by installing:

1. [Hadoop](installation/HADOOP.md)
1. [Spark](installation/SPARK.md)
1. [Dask](installation/DASK.md)


You're now ready to [run the benchmarks](../benchmark/README.md).