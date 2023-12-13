-- lists all records of the table second_table
-- of the database hbtn_0c_0 in your MySQL server.

-- Set the database name
SET @db_NAME = ARGV(0);
SET @table_NAME = 'second_table';

-- List all records of the second_table ordered by score
-- Construct the query and execute it
SET @query = CONCAT('
    SELECT score, name
    FROM ', @db_NAME, '.', @table_NAME, '
    ORDER BY score DESC;
');

-- Execute the query
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
