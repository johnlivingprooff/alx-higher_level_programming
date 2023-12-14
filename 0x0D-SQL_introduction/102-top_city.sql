-- Display top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT
    city,
    AVG((temperature_celsius * 9/5) + 32) AS average_temperature_fahrenheit
FROM
    temperature_data
WHERE
    MONTH(date) IN (7, 8)  -- July and August
GROUP BY
    city
ORDER BY
    average_temperature_fahrenheit DESC
LIMIT 3;
