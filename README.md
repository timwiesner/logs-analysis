# Udacity Full Stack Web Developer Nanodegree

##Logs Analysis Project

###Project Overview
This project uses psycopg2 as a PostgreSQL adapter for Python to run queries against a fictional news website database. These queries answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Installation Prerequisites
To run these queries, the following programs must be installed:
1. Python 3 https://www.python.org/downloads/
2. Virtual Box https://www.virtualbox.org/wiki/Downloads
3. Vagrant https://www.vagrantup.com/downloads.html

<!-- ### Installing the Repository


### Starting the Virtual Machine


### Installing the Database


### Required Database Views -->


Run Queries:
psql -d news -f newsdata.sql

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
