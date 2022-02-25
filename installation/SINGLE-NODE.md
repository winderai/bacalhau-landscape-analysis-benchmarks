# Single node installation

This set up is straightforward since you work only on a single host.
We're going to install:

- Pandas
- Dask
- Postgres
- Hadoop
- Spark
- Snowflake **???**

Proceed by installing each framework and related prerequistes by running the following script. 
Please DO NOT launch any cluster (yet).

```bash
cd installation/
bash install-single-node.sh
source ~/.bashrc
```

At this point we have all frameworks installed.

You're now ready to [run the benchmarks](../benchmark/README.md).