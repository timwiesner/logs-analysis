-- Delete before submission!!!


-- Query One
SELECT
	CONCAT(initcap(articles.title), ' - ', count(*), ' views')
FROM log
RIGHT JOIN articles
	ON substring(path, 10) = articles.slug
GROUP BY articles.title
ORDER BY log.count DESC
LIMIT 3;

-------------------------------------------------------------------

-- View for Query Two
CREATE VIEW most_accessed AS
SELECT articles.author, count(*)
FROM log
RIGHT JOIN articles
	ON substring(path, 10) = articles.slug
GROUP BY articles.author
ORDER BY log.count DESC;

-- Query Two
SELECT authors.name, SUM(most_accessed.count)
FROM most_accessed
JOIN authors
	ON most_accessed.author = authors.id
GROUP BY authors.name
ORDER BY SUM(most_accessed.count) DESC;

-------------------------------------------------------------------
-- QUERY THREE

-- Query Three Error View
CREATE VIEW failed_requests AS
  SELECT
    to_char(time, 'FMMonth, DD YYYY') AS date,
    COUNT(*) as err
  FROM log
  WHERE status like '404 NOT FOUND'
  GROUP BY date
  ORDER BY date

CREATE VIEW success_requests AS
  SELECT
    to_char(time, 'FMMonth, DD YYYY') AS date,
    COUNT(*) as ok
  FROM log
  WHERE status like '200 OK'
  GROUP BY date
  ORDER BY date;

SELECT
  CONCAT(
  success_requests.date, ' - ',
  round(CAST
      (failed_requests.err / success_requests.ok::float * 100
      AS numeric), 1),
      '% errors')
FROM success_requests
JOIN failed_requests
  ON success_requests.date = failed_requests.date
WHERE (failed_requests.err * 100) > success_requests.ok
