- not parallel
- can't concat to a signle table -> different schema!
- 

Prereqs:

pip install csvkit
pip install psycopg2

```
dropdb derivative-dataset
createdb derivative-dataset

for f in data/*.csv; do csvsql --db postgresql://127.0.0.1/derivative-dataset --insert "$f"; done

psql -d derivative-dataset -c "\d"




list=($(psql -d derivative-dataset --tuples-only -c "\d" | awk  '{ print $3 }'))
for f in $list; do psql -d derivative-dataset -c "Copy (SELECT * FROM \"$f\" LIMIT 10) To '/dev/null' With CSV DELIMITER ',' HEADER;"; done
```