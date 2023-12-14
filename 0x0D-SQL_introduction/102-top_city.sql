-- Display top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE MONTH = 7 OR MONTH = 8  -- July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
