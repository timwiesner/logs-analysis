#!/usr/bin/env python3

import psycopg2


def failed_requests():
    """Return '404 NOT FOUND' requests from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "CREATE VIEW failed_requests AS \
        SELECT \
            to_char(time, 'FMMonth, DD YYYY') AS date, \
            COUNT(*) as err \
        FROM log \
        WHERE status like '404 NOT FOUND' \
        GROUP BY date \
        ORDER BY date")
    conn.commit()
    cur.close()
    conn.close()

failed_requests()


def success_requests():
    """Return '200 OK' requests from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "CREATE VIEW success_requests AS \
        SELECT \
            to_char(time, 'FMMonth, DD YYYY') AS date, \
            COUNT(*) as ok \
        FROM log \
        WHERE status like '200 OK' \
        GROUP BY date \
        ORDER BY date")
    conn.commit()
    cur.close()
    conn.close()

success_requests()
