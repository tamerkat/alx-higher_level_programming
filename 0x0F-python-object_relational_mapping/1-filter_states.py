#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    curser = db.cursor()
    curser.execute("SELECT * FROM stats ORDER BY id ASC")
    rows = curser.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)
    curser.close()
    db.close()
