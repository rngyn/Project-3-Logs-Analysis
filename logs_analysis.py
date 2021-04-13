#!/usr/bin/env python2

import psycopg2


# connect to database
def run_query(query):
    db = psycopg2.connect('dbname=news')
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


# 1. What are the most popular three articles of all time?
def top_articles():
    query = '''select articles.title, count(*) as num from articles
        join log on log.path like concat('/article/%', articles.slug)
        group by articles.title
        order by num desc limit 3;'''

    results = run_query(query)

    for i in results:
        title = i[0]
        views = '" -- ' + str(i[1]) + " views"
        print("  " + u'\u2022' + " " + '"' + title + views)


# 2. Who are the most popular article authors of all time?
def top_authors():
    query = '''select authors.name, count(*) as num from authors
        join articles on authors.id = articles.author
        join log on log.path like concat('/article/%', articles.slug)
        group by authors.name
        order by num desc;'''

    results = run_query(query)

    for i in results:
        print("  " + u'\u2022' + " " + i[0] + ' -- ' + str(i[1]) + " views")


# 3. On which days did more than 1% of requests lead to errors?
def error_days():
    query = '''select total.day,
        round(((errors.error_requests*1.0)/total.requests), 3) as percent
        from (select date_trunc('day', time) "day", count(*) as error_requests
            from log where status like '404%' group by day) as errors
        join (select date_trunc('day', time) "day", count(*) as requests
            from log group by day) as total
        on total.day = errors.day
        where (round(((errors.error_requests*1.0)/total.requests), 3) > 0.01)
        order by percent desc;'''

    results = run_query(query)

    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print("  " + u'\u2022' + " " + date + " -- " + errors)


# print results
print('\nFinding all time most popular three articles...')
top_articles()
print('\nFinding all time most popular article authors...')
top_authors()
print('\nFinding which days did more than 1% of requests lead to errors...')
error_days()
