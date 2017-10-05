#!/usr/bin/env python3

import psycopg2


def query_one():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute("SELECT \
                    initcap(articles.title), \
                    most_accessed.count \
                 FROM most_accessed \
                 JOIN articles \
                 ON most_accessed.substring = articles.slug \
                 ORDER BY count DESC \
                 LIMIT 3")
    rows = cur.fetchall()
    print("Top Three Articles:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

query_one()
