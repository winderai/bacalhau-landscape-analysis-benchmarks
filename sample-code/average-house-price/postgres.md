```
dropdb averagehouseprice
createdb averagehouseprice

csvsql --verbose --db postgresql://127.0.0.1/averagehouseprice --insert data/address_book.csv --tables addressbook


psql -d averagehouseprice -c "\d"


psql -d averagehouseprice -c "SELECT * FROM addressbook LIMIT 10;"


psql -d averagehouseprice -c "SELECT \"Zipcode\", AVG(\"Price\") FROM addressbook GROUP BY \"Zipcode\" LIMIT 10;"