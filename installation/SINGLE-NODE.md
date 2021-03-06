# Single node installation

This setup is straightforward since you work only on a single host.
We're going to install:

- Pandas
- Dask
- Postgres
- Hadoop
- Spark
- Snowflake client



1) As first step, please install the [prerequistes setup for Snowflake](./SNOWFLAKE.md#prerequisites).
Note, do only the prerequistes part, not the client installation.
That'll install the right Snowflake client and configuration (e.g. account, db name, etc.).
The single-node install script will pick that up automatically.

2) Proceed by installing each framework and related prerequistes by running the following script (process duration ~7 minutes).
Please DO NOT launch any cluster (yet).

```bash
cd installation/
bash install-single-node.sh # confirm/proceed when prompted
source ~/.bashrc
```
At this point we have all frameworks installed.

If you'd like to track cpu/mem/etc. usage don't forget to set up [CloudWatch agent](./CLOUDWATCH.md).
After that, you'll be ready to [run the benchmarks](../benchmark/README.md).
