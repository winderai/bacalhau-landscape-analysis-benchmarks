# Multi node installation

This set up involves a number of steps run across multiple hosts.
Brew a :coffee: and take your time. 
You'll need to ssh into each node. 
Some commands will be issued on all hosts, others will be only for the master or slave(s), depending on the step.
Rest assured, each snippet makes its target host explicit either in the title, or in the description.

> Throughout these benchmarks we use the `master/slave` terminology only for legacy reasons (most Hadoop's instructions used that jargon). Winder.ai condemns any perpetration of slavery and therefore suggest the use of `main/worker` terminology in any future work.


For convienence, I'd recommend using [iTerm2's broadcast input](https://christopher.su/notes/mac/iterm-broadcast/) to quickly issue commands across multiple machines.
 
Proceed by installing:

1. [Hadoop](./HADOOP.md)
1. [Spark](./SPARK.md)
1. [Dask](./DASK.md)


If you'd like to track cpu/mem/etc. usage don't forget to set up [CloudWatch agent](./CLOUDWATCH.md).
After that, you'll be ready to [run the benchmarks](../benchmark/README.md).
