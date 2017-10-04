#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def query_one():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("select title, name from articles \
        join authors on articles.author = authors.id")
    rows = cur.fetchall()
    print("Show me the databases: ", cur.rowcount)
    for row in rows:
        print(row)
    cur.close()
    conn.close()

query_one()
