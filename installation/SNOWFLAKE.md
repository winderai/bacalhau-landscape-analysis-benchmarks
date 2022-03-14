


# Install SnowSQL

```
cd ~
curl -O https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowsql-1.2.21-linux_x86_64.bash
bash snowsql-1.2.21-linux_x86_64.bash 
```


# Configure client

```bash
export SNOW_ACCOUNTNAME=<YOUR_SNOWFLAKE_ACCOUNTNAME>
export SNOW_USERNAME=<YOUR_SNOWFLAKE_USERNAME>
export SNOW_PWD=<YOUR_SNOWFLAKE_PWD>
export SNOW_REGION=<YOUR_SNOWFLAKE_REGION>
export SNOW_DBNAME=<YOUR_SNOWFLAKE_DBNAME>
export SNOW_SCHEMANAME=<YOUR_SNOWFLAKE_SCHEMANAME>
export SNOW_WAREHOUSENAME=<YOUR_SNOWFLAKE_WAREHOUSENAME>
```

```bash
mkdir -p ~/.snowsql

echo "[connections]
accountname = ${SNOW_ACCOUNTNAME}
username = ${SNOW_USERNAME}
password = ${SNOW_PWD}
region = ${SNOW_REGION}
dbname = ${SNOW_DBNAME}
schemaname = ${SNOW_SCHEMANAME}
warehousename = ${SNOW_WAREHOUSENAME}

[variables]

[options]
auto_completion = True
log_file = ~/snowsql_rt.log
log_level = DEBUG
timing = True
output_format = psql
key_bindings = vi
repository_base_url = https://sfc-repo.snowflakecomputing.com/snowsql" > ~/.snowsql/config

chmod 700 ~/.snowsql/config
```


# Load

/home/ubuntu/bin/snowsql --query "PUT file://./data/wordcount.txt '@mystage';"


/home/ubuntu/bin/snowsql --query "COPY INTO WORDVALUE 
FROM '@mystage';"


/home/ubuntu/bin/snowsql --query "SELECT word, COUNT(*) as count
from (
  select c.value::string as word 
  from "WORDCOUNT2"."NEWSCHEMA"."WORDVALUE", 
        lateral flatten(input=>split(C1, ' ')) c
)
group by word
order by count desc
limit 10;"