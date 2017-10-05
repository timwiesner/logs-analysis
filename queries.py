#!/usr/bin/env python3

import psycopg2


def query_one():
    """Return top three accessed articles from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute("SELECT \
                    CONCAT(initcap(articles.title), ' - ', \
                    most_accessed.count, ' views') AS views \
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
    print('\n')
    conn.close()


def query_two():
    """Return top three accessed articles from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute("SELECT authors.name, articles.title \
                 FROM authors \
                 LEFT JOIN articles \
                    ON authors.id = articles.author")
    rows = cur.fetchall()
    print("Top Three Articles:")
    for row in rows:
        print(row)
    cur.close()
    print('\n')
    conn.close()







print('\n')

query_one()
query_two()
