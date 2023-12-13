-- removes all records with a score <= 5 in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.

-- Set the database name
SET @db_NAME = ARGV(0);
SET @table_NAME = 'second_table';

-- Display records before deletion
SELECT * FROM @db_NAME.@table_NAME;

-- Remove records with a score <= 5
DELETE FROM @db_NAME.@table_NAME
WHERE score <= 5;

-- Display records after deletion
SELECT * FROM @db_NAME.@table_NAME;
