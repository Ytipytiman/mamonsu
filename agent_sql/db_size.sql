select pg_database_size(datname::text) from pg_catalog.pg_database where datistemplate = false and datname = :'p1';