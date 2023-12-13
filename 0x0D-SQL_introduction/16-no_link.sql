-- lists all records of the table second_table

-- List records with a name and order by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;