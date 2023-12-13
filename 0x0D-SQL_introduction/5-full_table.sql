-- prints the full description of the table
-- first_table from the database hbtn_0c_0 in your MySQL server.

SET @db_NAME = ARGV(0);
SET @table_NAME = 'first_table';

-- Get the table information
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_schema = @db_NAME AND table_name = @table_NAME;
