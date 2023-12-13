-- lists all the tables of a database in your MySQL server.
SET @db_NAME := TRIM('mysql');
SHOW TABLES FROM @db_NAME;
