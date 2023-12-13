-- inserts a new row in the table first_table 
-- (database hbtn_0c_0) in your MySQL server.

SET @db_NAME = ARGV(0);
SET @table_NAME = 'first_table';

-- Insert a new row into the specified table
INSERT INTO @db_NAME.@table_NAME (id, name)
VALUES (89, 'Best School');
