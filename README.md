# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project

### Project Overview
This project uses Python 3 with psycopg2 as a PostgreSQL adapter to run queries against a fictional news website database. These queries answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Installation Prerequisites
To run these queries, the following programs must be installed:
* Python 3: https://www.python.org/downloads/
* Virtual Box: https://www.virtualbox.org/wiki/Downloads
* Vagrant: https://www.vagrantup.com/downloads.html

### Virtual Machine Configuration
* Download and unzip [Udacity's Vagrant Configuration File](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).

### Download Data
1. Download and unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Place `newsdata.sql` inside `FSND-Virtual-Machine/vagrant`. This directory can be found in the virtual machine installed in the previous step.

### Clone Repository
* Download/clone this repo and place the resulting `logs-analysis-master` folder inside `FSND-Virtual-Machine/vagrant` as well.

### Start Virtual Machine and Load Data
To run the Vagrant VM and load the news databse, `cd` into the `FSND-Virtual-Machine/vagrant` directory and enter the following commands into your terminal:
* `vagrant up` - This may take a few minutes, especially the first time.
* `vagrant ssh`
* `cd /vagrant`
* `psql -d news -f newsdata.sql`
* `psql -d news`

### Create Database Views
Copy and paste the following views in your PSQL terminal:

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

After creating these required views, type `\q` or hold `Ctrl+D` to exit the database.

### Run Queries
* Run the command `python3 logs-analysis-master/logs_analysis.py`.
* The output in your terminal should match included `example_output.txt` file.
