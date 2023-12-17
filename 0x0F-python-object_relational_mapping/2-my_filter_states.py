#!/usr/bin/python3
""" displays all values in the table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
