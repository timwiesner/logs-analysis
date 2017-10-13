#!/usr/bin/env python3

import psycopg2
import re



conn = psycopg2.connect(database="news")
cur = conn.cursor()


def print_rows(rows):
    for row in rows:
        # print(row)
        print('{} - {}'.format(row[0], row[1]))


def articles_query():
    """Return top three accessed articles from the database."""
    cur.execute("""
        SELECT
            initcap(articles.title),
            CONCAT(count(*), ' views')
        FROM log
        RIGHT JOIN articles
            ON substring(path, 10) = articles.slug
        GROUP BY articles.title
        ORDER BY log.count DESC
        LIMIT 3;""")
    rows = cur.fetchall()
    print("\nMost Popular Articles:")
    print_rows(rows)


def authors_query():
    """Return most popular article authors."""
    cur.execute("""
        SELECT
            authors.name,
            CONCAT(SUM(most_accessed.count), ' views')
        FROM most_accessed
        JOIN authors
            ON most_accessed.author = authors.id
        GROUP BY authors.name
        ORDER BY SUM(most_accessed.count) DESC""")
    rows = cur.fetchall()
    print("\nMost Popular Authors:")
    print_rows(rows)


def errors_query():
    """Return days where more than 1% of requests lead to errors."""
    cur.execute("""
        SELECT
            CONCAT(
            success_requests.date, ' - ',
            round(CAST
                (failed_requests.err / success_requests.ok::float * 100
                AS numeric), 1),
                '% errors')
        FROM success_requests
        JOIN failed_requests
            ON success_requests.date = failed_requests.date
        WHERE (failed_requests.err * 100) > success_requests.ok""")
    rows = cur.fetchall()
    print("\nDays With > 1% Request Errors:")
    print_rows(rows)


if __name__ == '__main__':
    articles_query()
    authors_query()
    # errors_query()
    cur.close()
    conn.close()
