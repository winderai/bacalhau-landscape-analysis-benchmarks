# Single node installation

This set up is straightforward since you work only on a single host.
We're going to install:

- Pandas
- Dask
- Postgres
- Hadoop
- Spark
- Snowflake

Let's start by setting up some environment variables for Snowflake.

```bash
export SNOW_ACCOUNTNAME=<YOUR_SNOWFLAKE_ACCOUNTNAME>
export SNOW_USERNAME=<YOUR_SNOWFLAKE_USERNAME>
export SNOW_PWD=<YOUR_SNOWFLAKE_PWD>
export SNOW_REGION=<YOUR_SNOWFLAKE_REGION>
export SNOW_DBNAME=<YOUR_SNOWFLAKE_DBNAME>
export SNOW_SCHEMANAME=<YOUR_SNOWFLAKE_SCHEMANAME>
export SNOW_WAREHOUSENAME=<YOUR_SNOWFLAKE_WAREHOUSENAME>
```

Proceed by installing each framework and related prerequistes by running the following script (process duration ~7 minutes).
Please DO NOT launch any application cluster (yet).


```bash
cd installation/
bash install-single-node.sh # confirm/proceed when prompted
source ~/.bashrc
```

At this point we have all frameworks installed.

You're now ready to [run the benchmarks](../benchmark/README.md).