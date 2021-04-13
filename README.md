# Logs Analysis Project
This application executes three SQL queries and returns the filtered results
from the database. The database contains newspaper articles, authors, as well
as web server logs. The three SQL queries answers the following questions:

1. **What are the most popular three articles of all time?**
2. **Who are the most popular article authors of all time?**
3. **On which days did more than 1% of requests lead to errors?**

## Files
* `logs_analysis.py` contains all code required to connect to the database, as
well as answer the three questions.

## Dependencies
[Python 2.7](https://www.python.org/downloads/) must be installed.

The application runs on a virtual machine using [Vagrant](https://www.vagrantup.com/).

[VirtualBox](https://www.virtualbox.org/) is also required to properly run the
virtual machine.

To properly setup the virtual machine, Udacity's vagrant files from their [GitHub](https://github.com/udacity/fullstack-nanodegree-vm)
is required.

Finally, the [SQL database file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
is needed as it contains all the articles the application would look through.

## Microsoft Windows Instructions
1. Unzip the SQL database file and place the `newsdata.sql` in the vagrant
directory of Udacity's `fullstack-nanodegree-vm` folder.

2. Place the project file `logs_analysis.py` in the same vagrant directory.  

3. Navigate to the vagrant directory and start a command prompt window; execute
`vagrant up`.

4. Once the process is completed, execute `vagrant ssh`.

5. Access the files within vagrant by typing `cd /vagrant`.

6. Now you can access the database by using the command
`psql -d news -f newsdata.sql`.

7. Once the database has been accessed, run the application with the command
`python logs_analysis.py`.

8. After a moment, the application should print out the results.

## Disclaimer
This application was written by Robert Nguyen with the help and guidance
of Udacity's Full Stack Web Developer Nanodegree Program.
