-- displays the number of records with id = 89 in the table first_table

SET @db_NAME = ARGV(0);
SET @table_NAME = 'first_table';

-- Count the number of records with id = 89
SELECT COUNT(*) AS num_records
FROM @db_NAME.@table_NAME
WHERE id = 89;
