-- lists the number of records with the same score in the table second_table

-- List the number of records by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;