#!/bin/bash

# fail fast
set -euxo pipefail


/home/ubuntu/bin/snowsql --query "SELECT word, COUNT(*) as count
from (
  select c.value::string as word 
  from "WORDCOUNT2"."NEWSCHEMA"."WORDVALUE", 
        lateral flatten(input=>split(C1, ' ')) c
)
group by word
order by count desc
limit 10;"