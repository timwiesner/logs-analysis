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
