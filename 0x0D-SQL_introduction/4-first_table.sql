-- creates a table called first_table in the current database in your MySQL server.

-- Set the database name
SET @db_NAME = ARGV(0);

-- Create the table first_table if it doesn't exist
SET @query = CONCAT('
    CREATE TABLE IF NOT EXISTS ', @db_NAME, '.first_table (
        id INT,
        name VARCHAR(256)
    );
');

-- Execute the query
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
