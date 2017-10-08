#!/usr/bin/env python3

import psycopg2


def most_accessed():
    """Return most accessed articles from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "CREATE VIEW most_accessed AS \
        SELECT articles.author, count(*) \
        FROM log \
        RIGHT JOIN articles \
            ON substring(path, 10) = articles.slug \
        GROUP BY articles.author \
        ORDER BY log.count DESC")
    conn.commit()
    cur.close()
    conn.close()

most_accessed()


def failed_requests():
    """Return '404 NOT FOUND' requests from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "CREATE VIEW failed_requests AS \
        SELECT \
            to_char(time, 'Month, DD YYYY') AS date, \
            COUNT(*) as err \
        FROM log \
        WHERE status like '404 NOT FOUND' \
        GROUP BY date \
        ORDER BY date")
    conn.commit()
    cur.close()
    conn.close()

failed_requests()
