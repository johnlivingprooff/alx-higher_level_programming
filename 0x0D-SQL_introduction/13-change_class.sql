-- removes all records with a score <= 5 in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.

-- Display records before deletion
SELECT * FROM second_table;

-- Remove records with a score <= 5
DELETE FROM second_table
WHERE score <= 5;

-- Display records after deletion
SELECT * FROM second_table;
