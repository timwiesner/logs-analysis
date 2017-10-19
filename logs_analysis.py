#!/usr/bin/env python3

import psycopg2


def retrieve(query):
    """Connect to database then execute query."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def print_rows(rows):
    """Print query retrieved from database."""
    for row in rows:
        print(" {} - {}".format(row[0], row[1]))


def articles_query():
    """Return top three accessed articles from the database."""
    articles = """
        SELECT
            initcap(articles.title),
            CONCAT(count(*), ' views')
        FROM log
        RIGHT JOIN articles
            ON substring(path, 10) = articles.slug
        GROUP BY articles.title
        ORDER BY log.count DESC
        LIMIT 3;"""
    rows = retrieve(articles)
    print("\nMost Popular Articles:")
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
                ON substring(path, 10) = articles.slug
            GROUP BY articles.author
            ) AS most_accessed
        WHERE authors.id = most_accessed.author
        GROUP BY authors.name
        ORDER BY SUM(most_accessed.count) DESC;"""
    rows = retrieve(authors)
    print("\nMost Popular Authors:")
    print_rows(rows)


def errors_query():
    """Return days where more than 1% of requests lead to errors."""
    errors = """
        SELECT
            success_requests.date,
            CONCAT(round(CAST
                (failed_requests.err / success_requests.ok::float * 100
                AS numeric), 1), '% errors')
        FROM success_requests
        JOIN failed_requests
            ON success_requests.date = failed_requests.date
        WHERE (failed_requests.err * 100) > success_requests.ok;"""
    rows = retrieve(errors)
    print("\nDays With > 1% Request Errors:")
    print_rows(rows)


if __name__ == '__main__':
    articles_query()
    authors_query()
    errors_query()
