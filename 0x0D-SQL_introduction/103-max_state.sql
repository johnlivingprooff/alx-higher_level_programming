-- Display max temperature of each state ordered by state name
SELECT
    state,
    MAX((temperature_celsius * 9/5) + 32) AS max_temperature_fahrenheit
FROM
    temperature_data
GROUP BY
    state
ORDER BY
    state;
