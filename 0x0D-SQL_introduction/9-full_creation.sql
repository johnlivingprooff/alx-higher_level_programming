-- creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server and add multiples rows.


-- Create the second_table if it doesn't exist

CREATE TABLE IF NOT EXISTS ', @db_NAME, '.', @table_NAME, ' (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Add multiple rows to the second_table

INSERT INTO ', @db_NAME, '.', @table_NAME, ' (id, name, score)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
