-- updates the score of Bob to 10 in the table second_table.

-- Set the database name
SET @db_NAME = ARGV(0);
SET @table_NAME = 'second_table';

-- Update the score of Bob to 10
UPDATE @db_NAME.@table_NAME
SET score = 10
WHERE name = 'Bob';
