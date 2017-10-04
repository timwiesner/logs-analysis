import psycopg2

DBNAME = "news"

def get_posts():
	"""Return relevant queries from the database."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("")
  posts = c.fetchall()
  db.close()
  return posts
