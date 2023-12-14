-- Display top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS average_temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- July and August
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
