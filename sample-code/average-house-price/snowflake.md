- must define schema first


# https://docs.snowflake.com/en/user-guide/data-load-web-ui.html#step-1-opening-the-load-data-wizard


1) create db
2) create schema
3) create file format
4) follow procedure for Loading Data -> https://docs.snowflake.com/en/user-guide/data-load-web-ui.html#step-1-opening-the-load-data-wizard



SELECT * FROM "TESTDB"."TESTSCHEMA"."DBTESTTABLE";


SELECT Zipcode, AVG(Price) FROM "TESTDB"."TESTSCHEMA"."DBTESTTABLE" GROUP BY Zipcode ORDER BY Zipcode ASC LIMIT 10;