SET @db_NAME = 'hbtn_0c_0';
SET @query = CONCAT('DROP DATABASE IF EXISTS ', @db_NAME);
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
