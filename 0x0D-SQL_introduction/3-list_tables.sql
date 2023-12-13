-- lists all the tables of a database in your MySQL server.

-- Set the database name
SET @db_NAME := TRIM('mysql');

-- Construct the query and execute it
SET @query = CONCAT('
    SHOW TABLES FROM ', @db_NAME, ';
');

-- Execute the query
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
