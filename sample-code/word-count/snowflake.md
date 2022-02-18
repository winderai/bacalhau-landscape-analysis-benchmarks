# Snowflake Word Count

## Prerequisite

### Create db

![alt text](imgs/snowflake_create_db.png "create db")

### Create schema

![alt text](imgs/snowflake_create_schema.png "create schema")

### Create file format

![alt text](imgs/snowflake_create_fileformat.png "create file format")

### Load wordcount.txt

Follow the procedure from the official docs: https://docs.snowflake.com/en/user-guide/data-load-web-ui.html#step-1-opening-the-load-data-wizard


## Run query

```sql
SELECT word, COUNT(*) as count
from (
  select c.value::string as word 
  from "WORDCOUNT"."WORDCOUNTSCHEMA"."TEST2", 
        lateral flatten(input=>split(C1, ' ')) c
)
group by word
order by count desc;
```

Expected result:

![alt text](imgs/snowflake_query_result.png "query output")
