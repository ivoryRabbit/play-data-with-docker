#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE hive;
    CREATE USER hive WITH ENCRYPTED PASSWORD 'hive';
    GRANT ALL PRIVILEGES ON DATABASE hive TO hive;
EOSQL
