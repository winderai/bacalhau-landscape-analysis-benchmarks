#!/bin/bash

# fail fast
set -euxo pipefail

sudo -u postgres psql -d wordcountdb -c "SELECT word, COUNT(word) 
FROM wordcount 
GROUP BY word 
ORDER BY count DESC 
LIMIT 10;"