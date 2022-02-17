```
postgres -D /usr/local/var/postgres

wget -P /tmp https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt

createdb enricorotundo

psql -d enricorotundo

drop table wordcount;

create table wordcount(word text);

tr " " "\n" < /tmp/wordcount.txt | psql -d enricorotundo -c "COPY wordcount FROM stdin (delimiter ' ');"

SELECT * FROM wordcount LIMIT 15;

SELECT word, COUNT(word) FROM wordcount GROUP BY word ORDER BY count DESC LIMIT 10;
```