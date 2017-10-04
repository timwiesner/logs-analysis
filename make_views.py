#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def topthree_view():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute(
        "CREATE VIEW topthree AS \
         SELECT SUBSTRING(path, 10), COUNT(*) \
         FROM log \
         WHERE path LIKE '/article/%' \
         GROUP BY path \
         ORDER BY count DESC \
         LIMIT 3")
    rows = cur.fetchall()
    cur.close()
    conn.close()

topthree_view()
