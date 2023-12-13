-- lists all rows of the table first_table 
-- from the database hbtn_0c_0 in your MySQL server.

SET @db_NAME = ARGV(0);
SET @table_NAME = 'first_table';

-- List all rows of the specified table
SELECT *
FROM  @db_NAME.@table_NAME;
