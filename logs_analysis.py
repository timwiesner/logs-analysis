#!/usr/bin/env python3

import psycopg2


def retrieve(query):
    """1. Connect to database then execute query. Returns rows from db."""
    try:
        conn = psycopg2.connect(database='news')
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except:
        print('Error: database not found.')


def print_rows(rows):
    """Print query retrieved from database."""
    for row in rows:
        print(' {} - {}'.format(row[0], row[1]))


def articles_query():
    """Return top three accessed articles from the database."""
    articles = """
        SELECT
            initcap(articles.title),
            CONCAT(views, ' views')
        FROM (
            SELECT path, count(*) AS views
            FROM log
            GROUP BY log.path
            ) AS log
        RIGHT JOIN articles
            ON '/article/' || articles.slug = log.path
        ORDER BY views DESC
        LIMIT 3;"""
    rows = retrieve(articles)
    print('\nMost Popular Articles:')
    print_rows(rows)


def authors_query():
    """Return most popular article authors."""
    authors = """
        SELECT
            authors.name,
            CONCAT(SUM(most_accessed.count), ' views') AS views
        FROM authors, (
            SELECT articles.author, count(*)
            FROM log
            RIGHT JOIN articles
                ON '/article/' || articles.slug = log.path
            GROUP BY articles.author
            ) AS most_accessed
        WHERE authors.id = most_accessed.author
        GROUP BY authors.name
        ORDER BY SUM(most_accessed.count) DESC;"""
    rows = retrieve(authors)
    print('\nMost Popular Authors:')
    print_rows(rows)


def errors_query():
    """Return days where more than 1% of requests lead to errors."""
    errors = """
        SELECT * FROM(
            SELECT time::date AS date,
            round(100 * (COUNT(*) FILTER (WHERE status = '404 NOT FOUND') /
                COUNT(*)::numeric), 2) AS error_percent
            FROM log
            GROUP BY time::date
        ) a
        WHERE error_percent > 1;"""
    rows = retrieve(errors)
    print('\nDays With > 1% Request Errors:')
    print_rows(rows)


if __name__ == '__main__':
    articles_query()
    authors_query()
    errors_query()
