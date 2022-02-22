# Postgres Word Count

```bash
# make sure postgres is running
postgres -D /usr/local/var/postgres

createdb wordcountdb

# launch postgres terminal
psql -d wordcountdb
```

Run the following command:

```
create table wordcount(word text);
```

```bash
tr " " "\n" < ./data/wordcount.txt | psql -d wordcountdb -c "COPY wordcount FROM stdin (delimiter ' ');"
```

```sql
SELECT * FROM wordcount LIMIT 15;
```

```sql
SELECT word, COUNT(word) 
FROM wordcount 
GROUP BY word 
ORDER BY count DESC 
LIMIT 10;
```