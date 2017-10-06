#!/usr/bin/env python3

import psycopg2


def leaderboard():
    """Return relevant queries from the database."""
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

leaderboard()
