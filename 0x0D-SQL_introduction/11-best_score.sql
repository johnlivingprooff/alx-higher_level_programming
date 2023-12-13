-- lists all records with a score >= 10 in the table
-- second_table of the database hbtn_0c_0 in your MySQL server.

-- Set the database name
SET @db_NAME = ARGV(0);
SET @table_NAME = 'second_table';

-- List records with a score >= 10 ordered by score
SELECT score, name
FROM @db_NAME.@table_NAME
WHERE score >= 10
ORDER BY score DESC;
