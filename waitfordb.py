import MySQLdb

from time import sleep

dbhost='djmyskeldb'
dbuser='root'
dbpasswd='root'
dbname = 'djmyskel'

while True:
    try:
        con = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=dbname)
    except Exception as ex:
        print('mySQL not available - sleeping...\n')
        sleep(4)

    break

print("mySQL seems to be there... might still be in installation... so let's wait some more")
sleep(4)

while True:
    try:
        con = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=dbname)
    except Exception as ex:
        print('mySQL not available - sleeping...\n')
        sleep(4)

    print("Finally... mySQL seems to be ready!")
    break