-- creates the database hbtn_0c_0 in your MySQL server.
SET @db_NAME = 'hbtn_0c_0';
SET @query = CONCAT('CREATE DATABASE IF NOT EXISTS ', @db_NAME);
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
