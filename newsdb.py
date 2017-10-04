#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

def get_posts():
	"""Return relevant queries from the database."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, name from articles join authors on articles.author = authors.id")
  posts = c.fetchall()
  db.close()
  return posts
