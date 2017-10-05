#!/usr/bin/env python3

import psycopg2


def leaderboard():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "CREATE VIEW most_accessed AS \
         SELECT SUBSTRING(path, 10), COUNT(*) \
         FROM log \
         WHERE path LIKE '/article/%' \
         GROUP BY path \
         ORDER BY count DESC;")
    conn.commit()
    cur.close()
    conn.close()

leaderboard()


def popularity():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute("CREATE VIEW most_popular AS \
                 SELECT articles.author, articles.title, most_accessed.count \
                 FROM most_accessed \
                 RIGHT JOIN articles \
                    ON most_accessed.substring = articles.slug")
    conn.commit()
    cur.close()
    conn.close()

popularity()
