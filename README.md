# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project

### Project Overview
This project uses Python with psycopg2 as a PostgreSQL adapter to run queries against a fictional news website database. These queries answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Installation Prerequisites
To run these queries, the following programs must be installed:
* Python3: https://www.python.org/downloads/
* Virtual: Box https://www.virtualbox.org/wiki/Downloads
* Vagrant: https://www.vagrantup.com/downloads.html

### Virtual Machine Configuration
* Download and unzip [Udacity's Vagrant Configuration File](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).

### Download Data
1. Download and unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Place `newsdata.sql` inside the `vagrant` directory. This directory can be found in the virtual machine installed in the previous step.

### Start Virtual Machine and Load Data
To run the Vagrant VM and load the news databse, `cd` into the `vagrant` directory and enter the following commands into your terminal:
* `vagrant up`
* `vagrant ssh`
* `cd /vagrant`
* `psql -d news -f newsdata.sql`

### Create Views
To successfully execute these queries, the following views must be created in the PSQL terminal:

`CREATE VIEW failed_requests AS
SELECT
  to_char(time, 'FMMonth, DD YYYY') AS date,
  COUNT(*) as err
FROM log
WHERE status like '404 NOT FOUND'
GROUP BY date
ORDER BY date;`

`CREATE VIEW success_requests AS
  SELECT
    to_char(time, 'FMMonth, DD YYYY') AS date,
    COUNT(*) as ok
  FROM log
  WHERE status like '200 OK'
  GROUP BY date
  ORDER BY date;`

<!-- psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. -->
