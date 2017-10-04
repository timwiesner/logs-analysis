#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def query_one():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("SELECT \
                    articles.title, \
                    topthree.count \
                FROM topthree \
                JOIN articles \
                    ON topthree.substring = articles.slug \
                ORDER BY count DESC")
    rows = cur.fetchall()
    print("Top Three Articles:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

query_one()
