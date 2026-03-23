-- Запрос на выборку
SELECT TrackId, Name, Composer,
	   Round(Milliseconds / 1000.0 / 60, 2) Minutes
FROM Track-- Запрос на выборку
SELECT TrackId, Name, Composer,
	   Round(Milliseconds / 1000.0 / 60, 2) Minutes
FROM Track
-- WHERE milliseconds BETWEEN 500000 AND 600000;
-- WHERE AlbumId In (7, 9, 45);
-- WHERE Name LIKE '%hell_%';
-- WHERE milliseconds >= 600000 AND name like '%a%';
WHERE Composer IS NOT NULL
ORDER BY Minutes ASC, Name DESC
LIMIT 10 OFFSET 5;

SELECT * FROM Album;

-- WHERE milliseconds BETWEEN 500000 AND 600000;
-- WHERE AlbumId In (7, 9, 45);
-- WHERE Name LIKE '%hell_%';
-- WHERE milliseconds >= 600000 AND name like '%a%';
WHERE Composer IS NOT NULL
ORDER BY Minutes ASC, Name DESC
LIMIT 10 OFFSET 5;

SELECT * FROM Album;
