-- creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server and add multiples rows.

-- Set the database name
SET @db_NAME = ARGV(0);
SET @table_NAME = 'second_table';

-- Create the second_table if it doesn't exist
SET @create_query = CONCAT('
    CREATE TABLE IF NOT EXISTS ', @db_NAME, '.', @table_NAME, ' (
        id INT,
        name VARCHAR(256),
        score INT
    );
');
PREPARE stmt_create FROM @create_query;
EXECUTE stmt_create;
DEALLOCATE PREPARE stmt_create;

-- Add multiple rows to the second_table
SET @insert_query = CONCAT('
    INSERT INTO ', @db_NAME, '.', @table_NAME, ' (id, name, score)
    VALUES
        (1, "John", 10),
        (2, "Alex", 3),
        (3, "Bob", 14),
        (4, "George", 8);
');
PREPARE stmt_insert FROM @insert_query;
EXECUTE stmt_insert;
DEALLOCATE PREPARE stmt_insert;
