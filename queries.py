#!/usr/bin/env python3

import psycopg2


def query_one():
    """Return top three accessed articles from the database."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "SELECT \
            CONCAT(initcap(articles.title), ' - ', count(*), ' views') \
        FROM log \
        RIGHT JOIN articles \
            ON substring(path, 10) = articles.slug \
        GROUP BY articles.title \
        ORDER BY log.count DESC \
        LIMIT 3")
    rows = cur.fetchall()
    text_file = open('query_results.txt', 'a')
    text_file.write('Top Three Articles:')
    for row in rows:
        text_file.write('\n {}'.format(row))
    text_file.close()
    cur.close()
    conn.close()


def query_two():
    """Return most popular article authors."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "SELECT \
            CONCAT(authors.name, ' - ', SUM(most_accessed.count), ' views') \
        FROM most_accessed \
        JOIN authors \
            ON most_accessed.author = authors.id \
        GROUP BY authors.name \
        ORDER BY SUM(most_accessed.count) DESC")
    rows = cur.fetchall()
    text_file = open('query_results.txt', 'a')
    text_file.write('\n \n Most Popular Article Authors:')
    for row in rows:
        text_file.write('\n {}'.format(row))
    text_file.close()
    cur.close()
    conn.close()


def query_three():
    """Return days where more than 1% of requests lead to errors."""
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    cur.execute(
        "SELECT \
            CONCAT( \
            success_requests.date, ' - ', \
            round(CAST \
                (failed_requests.err / success_requests.ok::float * 100 \
                AS numeric), 1), \
                '% errors') \
        FROM success_requests \
        JOIN failed_requests \
            ON success_requests.date = failed_requests.date \
        WHERE (failed_requests.err * 100) > success_requests.ok")
    rows = cur.fetchall()
    text_file = open('query_results.txt', 'a')
    text_file.write('\n \n Requests:')
    for row in rows:
        text_file.write('\n {}'.format(row))
    text_file.close()
    cur.close()
    conn.close()


if __name__ == '__main__':
    query_one()
    query_two()
    query_three()
